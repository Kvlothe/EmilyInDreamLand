from player import reset_player


def handle_player_object_collisions(player_rect, objects, score, player_pos, player_size, vy, on_ground):
    for obj_info in objects:
        obj_rect = obj_info["rect"]
        print(f"Object Type: {obj_info['type']}, Rect: {obj_rect}")  # Debug print
        if player_rect.colliderect(obj_rect):
            print(f"Collision detected with {obj_info['type']}")  # Debug print

            # Handle collision based on object type
            if obj_info["type"] == "gold_coin":
                score += 10  # Increase score for coins
                objects.remove(obj_info)  # Remove collected coin
            elif obj_info["type"] == "coin_box":
                score += 100
                objects.remove(obj_info)
            elif obj_info["type"] == "cactus":
                score = max(score - 10, 0)  # Deduct 10 points but not below 0
                reset_player()
            elif obj_info["type"] == "floating_block":
                # Check if player is on top of the block
                if player_rect.bottom <= obj_rect.top and player_pos[1] + player_size[1] < obj_rect.bottom:
                    player_pos[1] = obj_rect.top - player_size[1]
                    vy = 0
                    on_ground = True
                # Reset on_ground when not on block
                else:
                    on_ground = False

    return score, player_pos, vy, on_ground

