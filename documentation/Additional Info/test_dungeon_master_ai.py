import unittest
from config_loader import Config
from encounter_generator import EncounterGenerator
from npc_builder import NPCBuilder
from item_generator import ItemGenerator

class TestDungeonMasterAI(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.encounter = EncounterGenerator(self.config)
        self.npc = NPCBuilder(self.config)
        self.item = ItemGenerator(self.config)

    def test_encounter_generation(self):
        result = self.encounter.generate_encounter(3, 'forest', {})
        self.assertIn('encounter', result)
        self.assertIn('monsters', result['encounter'])

    def test_npc_builder(self):
        result = self.npc.build_npc('warrior', ['brave'], {})
        self.assertIn('npc', result)
        self.assertIn('stat_block', result)

    def test_item_generator(self):
        result = self.item.generate_item('rare', 'sword', {})
        self.assertIn('item', result)
        self.assertIn('lore', result)

if __name__ == '__main__':
    unittest.main()