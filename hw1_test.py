import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count(self) -> None:
        t1 = "audio" #output should be 4
        print(hw1.vowel_count(t1))
        t2 = "I like to study computer science" #output should be 11
        print(hw1.vowel_count(t2))

    # Part 2
    def test_short_lists(self) -> None:
        t1 = [[1, 2], [3, 4], [5, 6, 7]] #output should be [1, 2], [3, 4]
        print(hw1.short_lists(t1))
        t2 = [[1], [2], [3, 4], [5, 6], [7, 8, 9, 10, 11]] #output should be [3, 4], [5, 6]
        print(hw1.short_lists(t2))


    # Part 3
    def test_ascending_pairs(self) -> None:
        t1 = [[4, 2], [6, 7], [2, 1]] #output should be [[1, 2], [2, 4], [6, 7]]
        print(hw1.ascending_pairs(t1))
        t2 = [[6, 1], [5, 5], [0, 3], [7], [8]] #output should be [[0, 3], [1, 6], [5, 5], [7], [8]]
        print(hw1.ascending_pairs(t2))

    # Part 4
    def test_add_prices(self) -> None:
        t1 = data.Price(7, 40)
        t2 = data.Price(1, 30)
        r1 = hw1.add_prices(t1, t2) #output should be Price(8, 70)
        print(r1)
        t3 = data.Price(7, 60)
        t4 = data.Price(10, 80)
        r2 = hw1.add_prices(t3, t4)
        print(r2) #output should be Price(18, 40)

    # Part 5
    def test_rectangle_area(self) -> None:
        b1 = data.Rectangle(data.Point(4, 2), data.Point(5, 5))
        r1 = hw1.rectangle_area(b1) #output should be 3
        print(r1)
        b2 = data.Rectangle(data.Point(10, 10), data.Point(12, 12))
        r2 = hw1.rectangle_area(b2)  # output should be 4
        print(r2)



    # Part 6
    def test_books_by_author(self) -> None:
        booklist1 = [data.Book(["Author A"], "Food"),
                     data.Book(["Author B"], "Money"),
                     data.Book(["Author C"], "Ethics")]
        author1 = "Author A"
        print(hw1.books_by_author(booklist1, author1))
        booklist2 = [data.Book(["Author A"], "Time"),
                     data.Book(["Author C"], "Power")]
        author2 = "Author B"
        print(hw1.books_by_author(booklist2, author2))


    # Part 7
    def test_circle_bound(self) -> None:
        l1 = data.Point(0, 10)
        r1 = data.Point(10, 0)
        rectangle1 = data.Rectangle(l1, r1)
        circle1 = hw1.circle_bound(rectangle1) # output should be (5, 5) center + radius of 7.07
        print(circle1)
        l2 = data.Point(4, 3)
        r2 = data.Point(6, 7)
        rectangle2 = data.Rectangle(l2, r2)
        circle2 = hw1.circle_bound(rectangle2)  # output should be (5, 5) center + radius 2.24
        print(circle2)






    # Part 8
    def test_below_pay_average(self) -> None:
        e1 = [data.Employee("Sam", 40), data.Employee("Tate", 24),
              data.Employee("George", 100)]
        r1 = hw1.below_pay_average(e1) #output should be ["Sam", "Tate"]
        print(r1)
        e2 = [data.Employee("Theo", 100), data.Employee("Claire", 100),
              data.Employee("Emily", 100)]
        r2 = hw1.below_pay_average(e2) #output should be []
        print(r2)






if __name__ == '__main__':
    unittest.main()
