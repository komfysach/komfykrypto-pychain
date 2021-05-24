**Activate the virtual environment**
```
python3 -m blockchain-env\Scripts\activate
````

**Install all packages**
```

pip install -r requirements.txt
```

**Run the tests**

Make sure to activate the virtual environment.

```
python -m pytest backend/tests
```

**Run the application API**

Make sure to activate the virtual environment.

```
python -m backend.app
```

**Run a peer instance**

Make sure to activate the virtual environment.

Use Git Bash

```
export PEER=True && python -m backend.app
```

**Seed the backend with data**

Make sure to activate the virtual environment

```
export SEED_DATE=True && python -m backend.app
```
