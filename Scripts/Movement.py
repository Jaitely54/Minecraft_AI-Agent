import random
from mineflayer import Vec3

def setup_movement(bot):
    print('lee-mon is ready to move.')

    def random_walk():
        print('Starting random walk...')
        while True:
            x = bot.entity.position.x + random.randint(-10, 10)
            y = bot.entity.position.y
            z = bot.entity.position.z + random.randint(-10, 10)
            target = Vec3(x, y, z)

            print(f'Churan moving to: {target}')
            bot.move_to(target)

            time.sleep(4)  # Adjust the sleep time for how often Churan should move

    # Call the random walk function after bot has spawned
    bot.on_spawn(random_walk)
