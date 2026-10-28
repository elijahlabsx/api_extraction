from pathlib import Path

import pandas as pd
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
OUTPUT_PATH = Path("output") / "customers_clean.csv"

def fetch_users(url: str = API_URL, timeout: float = 10.0) -> list[dict]:
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()

        users = response.json()
        return users

    except requests.exceptions.Timeout:
        raise RuntimeError("The API request timed out.")

    except requests.exceptions.ConnectionError:
        raise RuntimeError("Could not connect to the API.")

    except requests.exceptions.HTTPError as exc:
        raise RuntimeError(f"HTTP request failed: {exc}")

    except requests.exceptions.JSONDecodeError:
        raise RuntimeError("The API returned invalid JSON.")

    except requests.exceptions.RequestException as exc:
        raise RuntimeError(f"API request failed: {exc}")


def describe_structure(payload) -> None:
    print("Payload type:", type(payload).__name__)

    if not payload:
        print("The payload is empty.")
        return

    print("Record type:", type(payload[0]).__name__)

    def print_types(data, parent_key=""):
        for key, value in data.items():
            full_key = f"{parent_key}.{key}" if parent_key else key

            print(f"{full_key}: {type(value).__name__}")

            if isinstance(value, dict):
                print_types(value, full_key)

    print_types(payload[0])


def extract_core_fields(users: list[dict]) -> list[dict]:
    core_users = []

    for user in users:
        record = {
            "id": user.get("id"),
            "name": user.get("name", ""),
            "email": user.get("email", ""),
            "city": user.get("address", {}).get("city", ""),
            "company": user.get("company", {}).get("name", ""),
        }

        core_users.append(record)

    return core_users


def build_structures(users: list[dict]) -> tuple[list, list[tuple], dict]:
    list_of_names = [user.get("name", "") for user in users]

    list_of_id_email = [
        (user.get("id"), user.get("email", ""))
        for user in users
    ]

    dict_of_id_city = {
        user.get("id"): user.get("address", {}).get("city", "")
        for user in users
    }

    return list_of_names, list_of_id_email, dict_of_id_city



def flatten_user(user: dict, parent_key: str = "", sep: str = "_") -> dict:
    flat = {}

    for key, value in user.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key

        if isinstance(value, dict):
            nested = flatten_user(value, new_key, sep)
            flat.update(nested)

        elif isinstance(value, list):
            for index, item in enumerate(value):
                item_key = f"{new_key}{sep}{index}"

                if isinstance(item, dict):
                    nested = flatten_user(item, item_key, sep)
                    flat.update(nested)
                else:
                    flat[item_key] = item

        else:
            flat[new_key] = value

    return flat



def to_dataframe(flat_users: list[dict]) -> pd.DataFrame:
    columns = [
        "customer_id",
        "name",
        "username",
        "email",
        "phone",
        "website",
        "address_street",
        "address_suite",
        "address_city",
        "address_zipcode",
        "address_geo_lat",
        "address_geo_lng",
        "company_name",
        "company_catchphrase",
        "company_bs",
    ]

    df = pd.DataFrame(flat_users)

    df = pd.DataFrame(flat_users)

    df = df.rename(columns={
        "id": "customer_id",
        "company_catchPhrase": "company_catchphrase",
    })

    df = df.reindex(columns=columns)

    df["customer_id"] = df["customer_id"].astype("Int64")
    df["address_geo_lat"] = pd.to_numeric(df["address_geo_lat"])
    df["address_geo_lng"] = pd.to_numeric(df["address_geo_lng"])

    return df


def export_csv(df: pd.DataFrame, path: Path = OUTPUT_PATH) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(path, index=False)
    return path

def main() -> None:
    try:
        users = fetch_users()
        describe_structure(users)

        core_users = extract_core_fields(users)
        print("Core fields extracted:", len(core_users))

        names, id_email, id_city = build_structures(users)

        flat_users = [flatten_user(user) for user in users]
        df = to_dataframe(flat_users)

        output_file = export_csv(df)

        print("CSV saved to:", output_file)
        print("Rows:", len(df))
        print("Columns:", len(df.columns))

    except (RuntimeError, ValueError, TypeError, KeyError) as exc:
        print(f"Error: {exc}")
        raise SystemExit(1)

if __name__ == "__main__":
    main()
    
    