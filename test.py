from utils.GuessEventType import guess_event_type

def test () -> None:
    x = guess_event_type('cs - init, page [analytics]')
    print(x)
    
test()