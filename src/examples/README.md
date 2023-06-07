# Yaml Knowledge is here

## FileName

Yaml file extension name are `.yaml` or `.yml` but for each project, you should follow the name convention.

## Dictionary

The basic of configuration languages is dictionary type. So, it's simple is that just `key` and `value`.

```yaml
name: John
age: 30
gender: male
```

## Map Objects

Similar to dictionary but in a key, there are some attribute inside a key.

```yaml
person:
  name: John
  age: 30
  gender: male
```

## Collection / List

At root level

```yaml
- Anakin
- Obi-Wan
- Padme
```

In a key

```yaml
charactors:
  - Anakin
  - Obi-Wan
  - Padme
```

List Obj

```yaml
charactors:
  - name: Anakin
    role: Jedi
  - name: Obi-Wan
    role: Jedi
  - name: Padme
    role: A princess
```

Single line list

```yaml
charactors: [ "Anakin", "Obi-Wan", "Padme" ]
```

## Combination map/obj/list

```yaml
charactors:
  - name: Anakin
    role: Jedi
    location:
      lat: 100.10
      long: 13.45
  - name: Obi-Wan
    role: Jedi
    location:
      lat: 101.10
      long: 15.45
  - name: Padme
    role: A princess
    location:
      lat: 110.10
      long: 15.45
```
