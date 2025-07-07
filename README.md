# bytecode-decompiler
credit to plusgiant for the API

# Bytecode Decompiler (Luau)

Petit script Python qui permet de décompiler en masse des fichiers `.luac` extraits avec `getscriptbytecode`, en utilisant l'API Konstant.

## ⚠️ Attention

Ce script ne fonctionne que si :

- Les `.luac` proviennent bien de `getscriptbytecode` via un exploit.
- L'API Konstant est disponible et accessible, (devrait etre up la majorité du temps).

---

## 🛠️ Prérequis

- [Python 3](https://www.python.org/downloads/)
- Le module `requests` (installation ci-dessous)

---

## 📦 Installation

1. Installer Python (cocher "Add Python to PATH" à l'installation)
2. Installer le module nécessaire :

```bash
py -m pip install requests

