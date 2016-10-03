import unittest
from tehai import getAtama,getTartsu,getShuntsu



class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        tehai = [[0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0],
        ]

        next_tehai = [[0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0],
        ]

        matched = {
            'atama':False,
            'ments':0
        }
        tehai,index,matched = getAtama(tehai,(0,0),matched)
        self.assertEqual(index, (0,8))
        self.assertEqual(tehai,next_tehai)
        self.assertEqual(matched['atama'],True)

    def test_mulit_array(self):
        tehai = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0],
        [0, 0, 0],
        ]
        matched = {
            'atama':False,
            'ments':0
        }
        tehai,index,matched = getAtama(tehai,(0,0),matched)
        self.assertEqual(index, (3,2))

    def test_get_tartsu(self):
        tehai = [[0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 4, 0],
        [3, 0, 0],
        ]
        matched = {
            'atama':False,
            'ments':0
        }
        tehai,index,matched = getTartsu(tehai,(0,0),matched)
        self.assertEqual(matched['ments'], 4)

    def test_get_shuntsu(self):
        tehai = [[0, 0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 1, 2, 0, 0, 0, 0],
        [0, 0, 4, 0],
        [3, 3, 3],
        ]
        matched = {
            'atama':False,
            'ments':0
        }
        tehai,index,matched = getShuntsu(tehai,(0,0),matched)
        self.assertEqual(matched['ments'], 2)


if __name__ == '__main__':
    unittest.main()
