from src.harness import run_case
import json

if __name__ == "__main__":
    res = run_case()
    print(json.dumps(res))
