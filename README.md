# FRIS: Firmware Risk Intelligence System (XAVION)

Prototype for a Viksit Bharat hackathon. **Demonstration mode only**: findings come from sample data in `src/data.ts`. No real firmware analysis is performed.

## Run
```bash
npm install && npm run dev            # http://localhost:5173
# optional backend (upload validation + SHA-256 only)
cd backend && python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && uvicorn main:app --port 8000
```
Works fully offline after install; the backend is optional.

## Architecture
- `src/data.ts`: sample assessment, baseline, scoring model (documented in the Risk prioritization page)
- `src/App.tsx`: all pages; state saved to localStorage
- `backend/main.py`: FastAPI. Streams uploads, enforces type and 64 MB limits, hashes, never executes or stores firmware

## Implemented
Dashboard, scanner (real file input, validation, staged demo scan), results with filters and detail, scoring model, remediation tracker (status, owner, notes, demo verification), printable report (use browser Print > Save as PDF), baseline comparison, About.

## Planned
Syft component inventory, NVD API and CISA KEV sync, SQLite/PostgreSQL storage, sandboxed unpacking worker, real rescan, split `App.tsx` into components and add tests.

## Data notes
CVE-2014-0160 and CVE-2021-3156 are real records; re-check details on NVD before citing. `FRIS-DEMO-*` entries are illustrative, not real CVEs.

## 3-minute demo flow
1. Dashboard: open risk and recent scan (20s). 2. Open sample results, review components (30s). 3. Click the Heartbleed finding, show the score breakdown (40s). 4. Read remediation (20s). 5. Remediation tracker: assign owner, Mark fixed (20s). 6. Run verification (20s). 7. Reports and Dashboard show updated counts (20s). 8. Baseline: show changed components (10s).
