# Top 5 Frequent Items Counter

Reads a text file and returns the 5 most frequent items.

---

## Setup

### Clone Repository

```bash
git clone <repository_url>
cd top-items-counter
```

### Create Environment File

```bash
cp .env.example .env
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python run.py
```

---

## Run Tests

```bash
pytest
```

---

## Docker

### Build Image

```bash
docker build -t top-items-counter .
```

### Run Container

```bash
docker run --rm top-items-counter
```

---

## Example Output

```text
apple: 100
banana: 90
orange: 80
grape: 70
mango: 50
```

---

## Project Structure

```text
src/
tests/
data/
Dockerfile
README.md
```

---

## Limitations

1. Assumes one item per line.
2. Case-sensitive counting.
3. Does not process binary files.
4. Entire frequency table is maintained in memory.
5. For extremely high-cardinality datasets, memory usage can become large.