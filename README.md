# dagster-cross-project

## Getting started 

```bash
pip install -e ".[dev]"
```

Then, start the Dagster UI web server:

```bash
dagster dev
```

If you are using conda and MacOS M1/M2, then you'll need to also run: 

```bash
pip uninstall grpcio
conda install grpcio
conda install grpcio-tools
```

## Example

### Materialize all 

Press "Materialize all" to materialize all dbt assets. 

### Materialize a subset of assets 

In the Dagster UI, apply the following search filter to materialize a subset of assets: 

```
person/serving/address+
```

Or you can run the following CLI command: 

```
dagster asset materialize -m dagster_project --select "person/serving/address+"
```

