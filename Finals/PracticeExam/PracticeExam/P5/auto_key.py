class AutoKeyContainer:
    pass


if __name__ == "__main__":
    # ALWAYS MAKE BETTER TESTS!!

    auto_key_container = AutoKeyContainer()
    key1 = auto_key_container.insert("First Value")
    key2 = auto_key_container.insert("Second Value")
    key3 = auto_key_container.insert("Third Value")
    key4 = auto_key_container.insert("Fourth Value")
    key5 = auto_key_container.insert("Fifth Value")

    print(auto_key_container.get(82398734))

    print("")
    print(auto_key_container.get(key3))
    print(auto_key_container.get(key2))
    print(auto_key_container.get(key5))
    print(auto_key_container.get(key4))
    print(auto_key_container.get(key1))

    auto_key_container.remove(key4)

    print("")
    print(auto_key_container.get(key3))
    print(auto_key_container.get(key2))
    print(auto_key_container.get(key5))
    print(auto_key_container.get(key4))
    print(auto_key_container.get(key1))

    auto_key_container.remove(key4)
