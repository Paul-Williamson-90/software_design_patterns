

"""
# Singleton Pattern

**Purpose:**
Ensures that a class has only one instance and provides a global point of access to it.

**When to Use:** 
When exactly one instance of a class is needed to coordinate actions across the system.

**Advantages:**
Controlled access to the single instance.
Reduced namespace usage.

**Disadvantages:**
Can be overused leading to bad design.
Hard to subclass.

**Use-Cases:**
Logger class.
Configuration manager.
Connection pool.

**Example in Python (Logger class use-case):**
"""

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ConfigManager(metaclass=SingletonMeta):
    def __init__(self):
        self._config = {}

    def set_config(self, key, value):
        self._config[key] = value

    def get_config(self, key):
        return self._config.get(key, None)

    def load_config_from_file(self, filepath):
        import json
        with open(filepath, 'r') as f:
            self._config = json.load(f)

    def save_config_to_file(self, filepath):
        import json
        with open(filepath, 'w') as f:
            json.dump(self._config, f, indent=4)


if __name__=="__main__":
    config_manager1 = ConfigManager()
    config_manager2 = ConfigManager()

    config_manager1.set_config('database_url', 'mysql://localhost:3306/mydb')
    
    print(config_manager2.get_config('database_url'))  