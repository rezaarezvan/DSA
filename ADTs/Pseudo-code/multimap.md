```
Multimap<Key, Value>:

    /*
    Just like the ordinary map - the multimap has Key-Value pairs.

    But in multimaps these values aren't a single value, it can be a whole collection of different values.
    */

    // Returns the whole collection of values associated with the key, k
    Collection<Value> get(Key k)

    // Adds the value, v, to the key, k
    void add(Key k, Value v)

    // Removes the value, v, associated with the key, k
    void remove(Key k, Value v)
```
