import unittest

import social

class TestBlog(unittest.TestCase):

    def test_generate_douban(self):
        BLOG_LIMIT = 5
        old_readme = social.DOUBAN_START_COMMENT + "old_content" + social.DOUBAN_END_COMMENT
        new_readme = old_readme
        print("BLOG_RSS_LINK:" )
        print("BLOG_LIMIT:" + str(BLOG_LIMIT))
        new_readme = social.generate_douban("186240167", BLOG_LIMIT, new_readme)
        print("new_readme:")
        print(new_readme)
        self.assertNotEqual(old_readme, new_readme)


if __name__ == '__main__':
    unittest.main()