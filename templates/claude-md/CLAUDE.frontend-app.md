# CLAUDE.md — Frontend app

## Project overview

TODO(team): What the app does, who uses it, the framework and rendering model (SPA / SSR / static).

## Commands

```bash
npm run dev
npm test
npm run lint
npm run build
```

## Conventions

- Components are small and typed; props are explicit (no spreading unknown objects into DOM elements).
- Server state goes through the data-fetching layer; do not call `fetch` directly in components.
- Styling follows the existing system (TODO(team): CSS modules / Tailwind / design tokens). Do not introduce a second approach.
- Accessibility is not optional: semantic elements, labels on inputs, visible focus, keyboard operability.
- No `any` in new code; no `// @ts-ignore` without a comment explaining why.

## Do not do without explicit approval

- Add or upgrade dependencies (bundle size is a budget)
- Change routing structure or auth/session handling
- Modify build or CI configuration

## Testing

- Component tests assert behavior (what the user sees/does), not implementation details.
- Run a single test: `TODO(team)`
