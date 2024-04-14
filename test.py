import pytest
import main

def test_initial_game_state():
    game = main.SnakeGame()
    
    # Check initial snake position
    assert game.snake_position == [100, 50]
    
    # Check initial snake body
    assert game.snake_body == [[100, 50], [90, 50], [80, 50]]
    
    # Check initial food position
    assert game.food_position in [[20, 20], [40, 20], [60, 20]]  # Assuming snake size is 20

def test_snake_movement():
    game = main.SnakeGame()
    
    # Move snake right
    game.change_direction('RIGHT')
    game.move_snake()
    assert game.snake_position == [120, 50]
    
    # Move snake down
    game.change_direction('DOWN')
    game.move_snake()
    assert game.snake_position == [120, 70]

def test_food_spawn():
    game = main.SnakeGame()
    
    # Simulate eating food
    game.snake_position = [40, 20]
    game.food_spawn = False
    game.move_snake()
    assert game.food_spawn == True

def test_game_over():
    game = main.SnakeGame()
    
    # Simulate snake collision with itself
    game.snake_body = [[100, 50], [90, 50], [80, 50], [80, 50]]
    with pytest.raises(SystemExit):
        game.check_collision()

    # Simulate snake going out of screen
    game.snake_position = [-10, 50]
    with pytest.raises(SystemExit):
        game.check_collision()

    game.snake_position = [610, 50]
    with pytest.raises(SystemExit):
        game.check_collision()

def test_direction_validation():
    game = main.SnakeGame()
    
    # Try to change direction to the opposite direction
    game.change
