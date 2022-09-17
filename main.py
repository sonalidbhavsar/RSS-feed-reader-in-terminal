
import feedparser
import const


def print_rss_entry(entry: dict) -> None:
    """
    Given the dict entry of RSS feed, prints the publication time, title, summary and link to article
    :param entry: RSS feed entry
    :return: None
    """
    print("-------------------------")
    if entry.get("published"):
        print(entry["published"])
    print(const.BOLD + entry["title"] + const.END)
    if entry.get("summary"):
        print(entry["summary"])
    if entry.get("link"):
        print("Link To Article: " + entry["link"])


def print_rss_feed_details(rss_url: str) -> None:
    """
    Prints the details of the RSS feed, given the RSS feed URL or string
    :param rss_url: the HTTP Url of the RSS feed
    :return: None
    """
    print()
    output = feedparser.parse(rss_url)
    if len(output.entries) == 0:
        print("No published articles from " + rss_url)
    else:
        print("Articles from " + rss_url + ":")
    for entry in output.entries:
        print_rss_entry(entry)
    print()


def main():
    rss_urls = input("Enter the RSS feed URLs separated by comma. Press Enter when done.\n")
    rss_urls_list = rss_urls.split(const.COMMA)
    for rss_url in rss_urls_list:
        rss_url = rss_url.strip()
        print_rss_feed_details(rss_url)
    print("-------------------------")


if __name__ == '__main__':
    main()
