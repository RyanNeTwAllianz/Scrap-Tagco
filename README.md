# Scrap-Tagco

### Doc

[TagCo Api](https://commandersact.github.io/api_doc/#operation/TmsWebTagsdestroy)

## Steps

Git clone the project and cd into it.

### First step

```bash
touch env.json
```

### Second step

Insert in the env.json
```
{
    "token": "Insert your token",
    "siteId": "Insert your site id,
    "baseUrl": "Insert your api url"
}
```

### Third step

```bash
python Main.py 
```

###  Run tests

```bash
python -m unittest discover -s test
```
