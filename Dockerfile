FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    STREAMLIT_SERVER_PORT=8080 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

WORKDIR /app

COPY requirements-wkala.txt requirements.txt ./
RUN pip install --no-cache-dir -r requirements-wkala.txt

# Backend + tools
COPY backend.py business_tools.py ./
# UI + prompt
COPY app.py prompt.txt test_app.py test_integration.py test_e2e_paid.py ./
# Carrier data (SKILL.md guidance and the published per-city tables)
COPY data/ ./data/

RUN useradd --create-home --uid 10001 appuser \
    && mkdir -p /app/data/store && chown -R appuser:appuser /app
USER appuser

EXPOSE 8080 8081

HEALTHCHECK --interval=30s --timeout=5s --start-period=25s --retries=3 \
    CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8080/_stcore/health',timeout=4).status==200 else 1)"

# One image, two processes: the customer backend on 8081 and the UI on 8080.
# In production put them behind one origin (see WKALA_INTEGRATION.md).
CMD ["sh", "-c", "uvicorn backend:app --host 0.0.0.0 --port 8081 & exec streamlit run app.py --server.port=8080 --server.address=0.0.0.0"]
