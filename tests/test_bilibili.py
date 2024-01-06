import unittest

import social

class TestBlog(unittest.TestCase):

    def test_generate_bilibili(self):
        BILIBILI_ID = '1802901'
        BLOG_LIMIT = 5
        old_readme = social.BILIBILI_START_COMMENT + "old_content" + social.BILIBILI_END_COMMENT
        new_readme = old_readme

        print("BLOG_RSS_LINK:" )
        print("BLOG_LIMIT:" + str(BLOG_LIMIT))
        new_readme = social.generate_bilibili_dynamic(BILIBILI_ID, BLOG_LIMIT, new_readme)
        print("new_readme:")
        print(new_readme)
        self.assertNotEqual(old_readme, new_readme)


if __name__ == '__main__':
    unittest.main()