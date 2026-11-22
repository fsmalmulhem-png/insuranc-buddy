# Tawuniya — provider data at a glance

## How many providers

**1,345 providers across 36 cities** in the Class A network.

## Where the network data lives

The **Tawuniya mobile app**, which exposes a provider list and a downloadable
PDF. The public website only shows an interactive map.

## Why it is not fetched automatically

The website blocks non-browser requests (403) and its download centre 404s. The
data sits behind the authenticated app. A policy holder supplied the PDF.

## Can this skill name a hospital?

**Yes — for Class A only.**

---

This file exists so every skill in the set has the same shape. The skills with
hospital tables — **GIG**, **Amana**, **Bupa**, **Gulf General** and now
**Tawuniya** — carry city files under `network/`.

Tawuniya was previously listed as publishing nothing. That was wrong: the data
is in the app, not on the website. See `network/README.md` for what changed and
why the automated checks missed it.
