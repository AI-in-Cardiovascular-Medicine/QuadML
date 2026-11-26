# Classification — Parameter tuning

Sets how QuadML searches the combinations you selected, then starts the run with **Start Procedure**.

![Parameter Tuning](../assets/class/Class33.png)

## Settings

| Setting | What it does |
|---------|--------------|
| **Search Budget** | **Fast** / **Balanced** / **Thorough** — how rich the search is (does not uncheck methods) |
| **Search algorithm** | **Grid Search** or **Random Search** (Random Search exposes **Iterations**) |
| **Cross-validation** | Fold method and number of splits inside Train |
| **Bootstrap CIs** | Optional 95% intervals on metrics (enable and re-run) |
| **CPU % / RAM %** | Resource limits (defaults often **50 / 50**) |
| **Imbalance Handling** | **Auto** / **On** / **Off**; balance strategy **None** or **SMOTE** when handling is active |

![Search settings](../assets/class/Class34.png)

## Running the search

**Start Procedure** checks that a run is not already active, the input and Output Directory are set, and the split is valid, then creates a new dated folder and launches the search. **Stop Procedure** cancels the run; partial results may remain, and **Rebuild Results** can rebuild `Final_Results.csv` from finished combo files when possible. Only one search can run at a time across modes.

![Start, Stop, and Rebuild](../assets/class/Class39.png)

## Tips

- Check the configuration tree before Start. Combination count is the product of every checked option
- Use **Fast** or **Balanced** for first runs
- Prefer **Stop Procedure** over closing the app

## Common mistakes

- Starting with every method selected
- Ignoring Resource Usage on large searches
- Setting CPU/RAM to 100% on a machine you still need for other work
- Starting again without noticing a new dated folder was created
