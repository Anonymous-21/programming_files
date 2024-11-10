#include <SFML/Graphics.hpp>
#include <raylib.h>
#include <string>
using namespace sf;

int main() {
  const int SCREEN_WIDTH = 800;
  const int SCREEN_HEIGHT = 600;
  const std::string SCREEN_TITLE = "Pong";
  const sf::Color SCREEN_BACKGROUND = sf::Color::White;
  const int GAME_FPS = 60;

  RenderWindow window(VideoMode(SCREEN_WIDTH, SCREEN_HEIGHT), SCREEN_TITLE);

  while (window.isOpen()) {
    Event event;
    while (window.pollEvent(event)) {
      if (event.type == sf::Event::Closed) {
        window.close();
      }
    }

    window.clear(SCREEN_BACKGROUND);

    window.display();
  }

  return 0;
}
