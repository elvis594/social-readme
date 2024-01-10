import unittest

import social

class TestBlog(unittest.TestCase):

    def test_generate_zhihu(self):
        BLOG_LIMIT = 5
        old_readme = social.ZHIHU_START_COMMENT + "old_content" + social.ZHIHU_END_COMMENT
        new_readme = old_readme
        print("BLOG_RSS_LINK:" )
        print("BLOG_LIMIT:" + str(BLOG_LIMIT))
        new_readme = social.generate_zhihu_dynamic("594-26", BLOG_LIMIT, new_readme)
        print("new_readme:")
        print(new_readme)
        self.assertNotEqual(old_readme, new_readme)


if __name__ == '__main__':
    unittest.main()