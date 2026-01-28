def move_num(test_str):
  num_str = ''.join(i for i in test_str if i.isdigit())
  else_str = ''.join(i for i in test_str if not i.isdigit())
  return else_str + num_str[:len(num_str)-1]

# Test Cases (Partial...):
def test_move_num_base():
    assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
    assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
    assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'