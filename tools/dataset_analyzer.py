from pathlib import Path
from collections import Counter
import matplotlib.pyplot as plt


DATASET_PATH = Path(r"datasets")

CLASS_NAMES = [
    "mouse_bite",
    "spur",
    "missing_hole",
    "short",
    "open_circuit",
    "spurious_copper",
]


def count_split(split):
    label_folder = DATASET_PATH / split / "labels"

    image_count = 0
    class_counter = Counter()

    for label_file in label_folder.glob("*.txt"):
        image_count += 1

        with open(label_file, "r") as f:
            for line in f:
                if line.strip() == "":
                    continue

                class_id = int(line.split()[0])
                class_counter[class_id] += 1

    return image_count, class_counter


def print_statistics():
    total_counter = Counter()

    for split in ["train", "val", "test"]:
        images, counter = count_split(split)

        total_counter.update(counter)

        print(f"\n===== {split.upper()} =====")
        print(f"Images : {images}")

        for class_id, name in enumerate(CLASS_NAMES):
            print(f"{name:<20} : {counter[class_id]}")

    print("\n===== TOTAL =====")

    total_instances = sum(total_counter.values())

    print(f"Instances : {total_instances}")

    for class_id, name in enumerate(CLASS_NAMES):
        print(f"{name:<20} : {total_counter[class_id]}")

    return total_counter


def plot_distribution(counter):
    labels = CLASS_NAMES
    values = [counter[i] for i in range(len(CLASS_NAMES))]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, values)
    plt.xticks(rotation=30)
    plt.ylabel("Instances")
    plt.title("PCB Dataset Class Distribution")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    counter = print_statistics()
    plot_distribution(counter)