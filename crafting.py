# Simple crafting system.

from typing import Union


version = 1.0

class Entity:
    def __init__(self, entity_name: Union[str, None]) -> None:
        """Create entity."""
        self.entity_name = entity_name

class Ceil:
    empty_ceil = Entity('empty')

    def __init__(self, entity: Entity) -> None:
        """Create ceil."""
        self.entity_inside_ceil = entity

class CraftingRecipe:
    def __init__(self, recipe: dict[int, Entity], result: Entity) -> None:
        """Create crafting recipe."""
        self.recipe = recipe
        self.result = result

    def do_recipe(recipe: dict) -> None:
        """Do recipe."""
        return recipe

class CraftingTable:
    def __init__(self) -> None:
        """Initialize crafting table."""
        self.entities = []
        self.ceils = []
        self.crafting_recipes = []

        self.ceils_lenght = 0

    def add_entity(self, entity: Entity) -> None:
        """Register new entity on the crafting table."""
        self.entities.append(entity)

    def add_ceil(self, ceil: Ceil) -> None:
        """Register new ceil on the crafting table."""
        self.ceils_lenght += 1

        self.ceils.append({self.ceils_lenght: ceil})

    def add_crafting_recipe(self, crafting_recipe: CraftingRecipe) -> None:
        """Register new crafting recipe on the crafting table."""
        self.crafting_recipes.append(crafting_recipe)

    def remove_object(self, obj: Union[Entity, Ceil, CraftingRecipe]) -> None:
        """Remove object from crafting table."""
        if obj == Entity:
            self.entities.pop()

        elif obj == Ceil:
            self.ceils.pop()

        elif obj == CraftingRecipe:
            self.crafting_recipes.pop()

    def update_ceil(self, ceil_pos: int, new_ceil: Ceil) -> None:
        """Update crafting table ceil."""
        if ceil_pos > self.ceils_lenght:
            return RuntimeError('trying to update ceil that doesn\'t exists')

        self.ceils[ceil_pos - 1] = new_ceil

    def matches_to_some_recipe(self, recipe: dict) -> bool:
        """Check if recipe matches to some recipe on the crafting table."""
        for crafting_recipe in self.crafting_recipes:
            crafting_recipe_entity_names = [entity.entity_name for entity in crafting_recipe.recipe.values()]
            crafting_recipe_with_entity_names = {pos: entity_name for pos, entity_name in zip(crafting_recipe.recipe.keys(), crafting_recipe_entity_names)}

            user_recipe_entity_names = [entity.entity_name for entity in recipe.values()]
            user_crafting_recipe_with_entity_names = {pos: entity_name for pos, entity_name in zip(recipe.keys(), user_recipe_entity_names)}

            if crafting_recipe_with_entity_names == user_crafting_recipe_with_entity_names:
                return True

        else:
            return False

    def get_result_from_recipe(self, recipe: dict, get_name: bool=False) -> bool:
        """Get result from recipe."""
        for crafting_recipe in self.crafting_recipes:
            crafting_recipe_entity_names = [entity.entity_name for entity in crafting_recipe.recipe.values()]
            crafting_recipe_with_entity_names = {pos: entity_name for pos, entity_name in zip(crafting_recipe.recipe.keys(), crafting_recipe_entity_names)}

            user_recipe_entity_names = [entity.entity_name for entity in recipe.values()]
            user_crafting_recipe_with_entity_names = {pos: entity_name for pos, entity_name in zip(recipe.keys(), user_recipe_entity_names)}

            if crafting_recipe_with_entity_names == user_crafting_recipe_with_entity_names:
                if get_name:
                    return crafting_recipe.result.entity_name

                return crafting_recipe.result

        else:
            return Entity(None)

    def craft(self, recipe: dict) -> bool:
        """Craft recipe."""
        return self.get_result_from_recipe(recipe, False)

    def craft_from_ceils(self) -> None:
        """Craft recipe from ceils."""
        recipe = {}

        for ceil in self.ceils:
            recipe = recipe | ceil

        recipe = {pos: entity.entity_inside_ceil for pos, entity in recipe.items()}

        return self.craft(recipe)
