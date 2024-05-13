favorite_languages = {
      'jen': ['python', 'rust'],
      'sarah': ['c'],
      'edward': ['rust', 'go'],
      'phil': ['python', 'haskell'],
      }

for name, languages in favorite_languages.items():    ##파이선의 딕셔너리와 리스트 for문의 기본임 알아두자
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")