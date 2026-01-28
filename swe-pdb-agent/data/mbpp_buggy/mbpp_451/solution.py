import re

def remove_whitespaces(text1):
  if not isinstance(text1, str):
    return ''
  text1 = text1.strip()
  text1 = text1.replace(' ', '')
  return text1[1:]

def test_remove_whitespaces_base():
    assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
    assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'
    assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift'