# codeforboston/police-data-trust context
> refreshed 2026-09-04 | upstream default: main @ 72059bf

## Identity & policies
- upstream: codeforboston/police-data-trust, default branch `main`, primary language Python (Flask/Neo4j backend) + TypeScript/Next.js frontend. English-first (issues/docs/UI all English).
- CLA/DCO: none found (no CLA bot, no contributor signup in CONTRIBUTING).
- AI-assisted PR policy: unstated (no AI ban/disclosure in repo or org `codeforboston/.github`).
- signed commits required: no.
- PR template: none (no `.github/PULL_REQUEST_TEMPLATE.md`; org `codeforboston/.github` has none either). Use pipeline 3-section fallback body.
- external tracker: GitHub issues.

## Conventions (verified from merged PRs)
- branch naming: mixed — `dmalone/<desc>`, `mikeyavorsky/<desc>`, `fix/<desc>` (e.g. `fix/507-officer-require-source`), `issue-<n>-<desc>`, `feature/<desc>`. `fix/<kebab-desc>` is acceptable.
- test command: frontend `npm run test:unit` (vitest), `npm run lint`, `npm run check-formatting`, `npm run check-types`; backend `python -m pytest` (needs Neo4j/docker).
- CI: GitHub Actions present (frontend lint/test/typecheck + backend). Fork Actions not connected (0 workflow runs on fork) — same fork-initialization artifact as other forks.
- outside PRs do get merged: paigebraun, maxaaronson, JMStudiosJoe, jestradasalinas, signalflowsean, mfoos all have merged PRs. Recent activity is maintainer-heavy (DMalone87, mikeyavorsky, pkhanna88).

## Maintainer picture
- active maintainers: DMalone87 (very active, most merges), mikeyavorsky, pkhanna88. Response latency: fast for maintainer PRs; external PRs merged within days-weeks.
- in-flight maintainer work: search UI filtering, caching, detail pages, complaints charts — avoid overlapping these areas.

## Issue-area health
- Open issues: 26. Most feature/bug issues are assigned or have open PRs.
- Unassigned + unclaimed candidates reviewed:
  - #518 [BUG] Refreshing Search Page "No access token available" — ALREADY FIXED by merged PR #546 (dmalone/search-auth-bug-fix, merged 2026-03-20). Issue left open but fix is in current code (SearchProvider guards on hasHydrated). NOT a pick.
  - #507 [BUG] Officer creation requires data source — has open PR #533 (TristanGramsch). Claimed.
  - #438/#437 [BUG] API doc incorrect — external readme.io doc mismatch; code+frontend are internally consistent. Doc is external, not fixable in-repo.
  - #416 [BUG] Incorrect response to lack of permission — vague repro, no maintainer engagement.
  - #362 deprecation warnings — broad, no maintainer engagement.

## Gap ledger (dedupe — READ FIRST, never re-pick)
- (none yet for this repo)

## Mined gaps (discovered, not yet attempted)
- 2026-09-04 `apiFetch` auth-hydration race: `frontend/utils/apiFetch.ts` retries `getAuth()` only 3x100ms and throws "No access token available" if the global auth snapshot isn't hydrated yet. PR #546 only patched SearchProvider to skip fetching until `hasHydrated`; the root cause in `apiFetch` remains and can affect any other caller (useAgencyOfficers, useAgencyUnits, useUnitOfficers, useProfile, page components) on a page refresh. Fix: add `hasHydrated` to the auth snapshot and have `apiFetch` wait for hydration (with a timeout) before falling back to refresh/error. Regression test: apiFetch called before hydration completes should wait and use the hydrated token. Dedupe: upstream PR search for "No access token"/"hydration"/"refresh"/"auth" returns no open/closed/merged PR fixing apiFetch itself (only #546 which fixed SearchProvider). — status: proposed
