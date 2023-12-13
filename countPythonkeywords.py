
import keyword as keywordList

def count_keywords(fileName):
    keywords = keywordList.kwlist

    keyword_counts = {kw: 0 for kw in keywords}

    with open(fileName, "r") as file:
        for line in file:
             for keyword in keywords:
                if keyword in line:
                 keyword_counts[keyword] += 1

    return keyword_counts

def main():
    filename = input("Enter the Python source code filename: ")
    keyword_counts = count_keywords(filename)

    if keyword_counts:
        print("Keyword Counts:")
        for keyword, count in keyword_counts.items():
            print(f"{keyword}: {count}")

if __name__ == "__main__":
    main()
