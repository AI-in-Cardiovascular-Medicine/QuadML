# Shared — Application shell

**Where**: Entire QuadML window

This page is the cross-mode chrome: Welcome, left navigation, theme, and how modes are switched. Pipeline step pages start at [File Selection](02-file-selection.md).

![QuadML Welcome](../assets/getting-started/welcome.png)

---

## What to click

### Welcome

1. On launch you land on **Welcome** until you open a mode step.
2. Expand a mode category on the left, then click a step (for example **File Selection**).

### Left navigation

3. Top-level categories: **Classification**, **Regression**, **Survival Analysis**, **Clustering**.
4. Click a category header to expand/collapse its steps.
5. Click a step name to show that page in the center stack.
6. Mode state is kept separately — switching modes does not wipe the other mode’s checkboxes and paths.

### Back / Next

7. Bottom **Back** and **Next** move through the **current** mode’s step order.
8. Use them for a linear pass; use the left nav to jump.

### Theme

9. Use the theme control (light / dark) in the chrome. Theme styling comes from shared theme helpers; the toggle lives on the main window.

### Logos and window title

10. Application branding and window title are set by the main window. Frozen builds use the packaged entry (`quadml_entry`) so search/worker children do not open a second GUI.

---

## Mode switching while a run is active

- Only one **Start Procedure** search may run at a time.
- If you try to start another mode’s search while one is running, QuadML warns you to switch to the running mode or **Stop Procedure** first.
- Progress, resource sampling, and Stop remain tied to the active run’s Parameter Tuning / Search Settings page.

---

## Process roles (background)

You normally only use the GUI role. Under the hood:

| Role | When |
|------|------|
| GUI | Default — main window |
| `search` | Child process for combinatorial search (`QUADML_ROLE=search`) so Stop can kill the process tree |
| `worker` | Outer combination workers |

Users do not set these manually in the UI. See also [Start, Stop, and resources](13-start-stop-and-resources.md).

---

## Common mistakes

- Expecting File Selection columns from Classification to apply after switching to Survival without re-checking duration/event roles
- Starting a second mode’s search while the first is still running
- Using Back/Next across modes — they follow the **current** mode’s order
