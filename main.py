import os

TEXT = "My agent entered forty bounties overnight, won none of them, and woke me up to call it 'momentum'."

def main():
    assert 1 <= len(TEXT) <= 200 and TEXT.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
