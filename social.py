import tools
import feedparser
import os
RSS_HUB_LINK = str(os.getenv("INPUT_RSS_HUB_LINK"))

BILIBILI_START_COMMENT = '<!-- START_SECTION:bilibili -->'
BILIBILI_END_COMMENT = '<!-- END_SECTION:bilibili -->'

ZHIHU_START_COMMENT = '<!-- START_SECTION:zhihu -->'
ZHIHU_END_COMMENT = '<!-- END_SECTION:zhihu -->'

DOUBAN_START_COMMENT = '<!-- START_SECTION:douban -->'
DOUBAN_END_COMMENT = '<!-- END_SECTION:douban -->'

def generate_douban(username, limit, readme) -> str:
    """Generate douban"""
    entries = feedparser.parse("https://www.douban.com/feed/people/" + username + "/interests")["entries"]
    arr = [
        {
            "title": item["title"],
            "url": item["link"].split("#")[0],
            "published": tools.format_time(item["published"]),
            "rating_star": tools.generate_rating_star(item["description"])
        }
        for item in entries[:limit]
    ]

    content = "\n".join(
        ["* <a href='{url}' target='_blank'>{title}</a> {rating_star}- {published}".format(**item) for item in arr]
    )

    return tools.generate_new_readme(DOUBAN_START_COMMENT, DOUBAN_END_COMMENT, content, readme)


def generate_zhihu_dynamic(user_id, limit, readme) -> str:
    """"Generate 知乎 dynamic"""
    entries = tools.generate_entries(RSS_HUB_LINK,"/zhihu/people/activities/",user_id)
    arr = [
        {
            "title": item["title"],
            "url": item["link"].split("#")[0],
        }
        for item in entries[:limit]
    ]

    content = "\n".join(
        ["* <a href='{url}' target='_blank'>{title}</a>".format(**item) for item in arr]
    )
    return tools.generate_new_readme(ZHIHU_START_COMMENT, ZHIHU_END_COMMENT, content, readme)


def generate_bilibili_dynamic(user_id, limit, readme) -> str:
    """"Generate bilibili dynamic"""
    entries = tools.generate_entries(RSS_HUB_LINK,"/bilibili/user/dynamic/",user_id)
    arr = [
        {
            "title": item["title"],
            "url": item["link"].split("#")[0],
        }
        for item in entries[:limit]
    ]

    content = "\n".join(
        ["* <a href='{url}' target='_blank'>{title}</a>".format(**item) for item in arr]
    )
    return tools.generate_new_readme(BILIBILI_START_COMMENT, BILIBILI_END_COMMENT, content, readme)


