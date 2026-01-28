from solution import *
import math

def test_all():
    p1 = Player("p1", 100)
    p2 = Player("p2", 120)
    p3 = Player("p3", 130)
    p4 = Player("p4", 150)
    p5 = Player("p5", 130)
    p6 = Player("p6", 200)
    p7 = Player("p7", 190)
    p8 = Player("p8", 140)

    n1 = TournamentTreeNode(p1, p2)
    n2 = TournamentTreeNode(p3, p4)
    n3 = TournamentTreeNode(p5, p6)
    n4 = TournamentTreeNode(p7, p8)

    n5 = TournamentTreeNode(n1, n2)
    n6 = TournamentTreeNode(n3, n4)

    root = TournamentTreeNode(n5, n6)
    root.play()
    assert root.who_won().name == "p6"

    p_test1 = Player("TestPlayer1", 50)
    assert p_test1.name == "TestPlayer1" and p_test1.rating == 50

    try:
        p_test_invalid = Player("TestPlayerInvalid", -10)
    except AssertionError:
        pass

    p_higher_rating = Player("High", 100)
    p_lower_rating = Player("Low", 50)
    p_equal_rating_higher_name = Player("Zeta", 75)
    p_equal_rating_lower_name = Player("Alpha", 75)

    assert p_higher_rating.against(p_lower_rating) == p_higher_rating

    assert p_lower_rating.against(p_higher_rating) == p_higher_rating

    assert p_equal_rating_higher_name.against(
        p_equal_rating_lower_name) == p_equal_rating_lower_name

    # lower name
    assert p_equal_rating_lower_name.against(
        p_equal_rating_higher_name) == p_equal_rating_lower_name

    tn_test1 = TournamentTreeNode(p_test1, p_higher_rating)
    assert isinstance(tn_test1.left, Player) and isinstance(
        tn_test1.right, Player)

    tn_test2 = TournamentTreeNode(tn_test1, p_lower_rating)
    assert tn_test2.who_won() is None

    tn_test2.play()
    assert tn_test2.who_won() == p_higher_rating

    tn_full_tournament = TournamentTreeNode(tn_test2, tn_test1)
    tn_full_tournament.play()
    assert tn_full_tournament.who_won() == p_higher_rating

    p_same_name_rating = Player("Equal", 100)
    assert p_same_name_rating.against(
        Player("Equal", 100)).name == p_same_name_rating.name

    p_zero_rating = Player("Zero", 0)
    p_high_rating = Player("High", 100000)
    assert p_zero_rating.against(p_high_rating) == p_high_rating
    assert p_high_rating.against(p_zero_rating) == p_high_rating

    tn_complex = TournamentTreeNode(
        TournamentTreeNode(p_zero_rating, p_high_rating),
        TournamentTreeNode(p_same_name_rating, p_equal_rating_lower_name)
    )
    tn_complex.play()
    assert tn_complex.who_won() == p_high_rating

    tn_complex.play()
    assert tn_complex.who_won() == p_high_rating

    p_max_rating = Player("Max", 2147483647)  # Assuming 32-bit int max
    tn_edge_case = TournamentTreeNode(p_zero_rating, p_max_rating)
    tn_edge_case.play()
    assert tn_edge_case.who_won() == p_max_rating

    left_child_node = TournamentTreeNode(p1, p2)
    right_child_player = p3
    tn_left_node = TournamentTreeNode(left_child_node, right_child_player)
    assert tn_left_node.who_won() is None

    left_child_player = p4
    right_child_node = TournamentTreeNode(p5, p6)
    tn_right_node = TournamentTreeNode(left_child_player, right_child_node)
    assert tn_right_node.who_won() is None

    left_child_node_2 = TournamentTreeNode(p7, p8)
    right_child_node_2 = TournamentTreeNode(p1, p2)
    tn_both_nodes = TournamentTreeNode(left_child_node_2, right_child_node_2)
    assert tn_both_nodes.who_won() is None
    import inspect

    class PlayerTest(Player):
        """
        A subclass of Player to override the against method for testing purposes.
        """

        def against(self, other: 'Player') -> 'Player':
            # Check if 'who_won' is in the call stack
            for frame_record in inspect.stack():
                if 'who_won' in frame_record.function:
                    self.found_who_won = True
                    break
            return super().against(other)

    player1 = PlayerTest("Player1", 100)
    player2 = PlayerTest("Player2", 80)

    player1.found_who_won = False

    node = TournamentTreeNode(player1, player2)
    winner = node.who_won()

    assert player1.found_who_won, "The method who_won did not call against."