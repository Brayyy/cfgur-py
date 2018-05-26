import cfgur

# Initialize once, pass in config
cfgur.init({
    "parser": {
      "description": "this is the service description"
    },
    "args": [
        {
            "name": "-test",
            "help": "Description of test",
            "default": "test-db",
            "required": False,
        }, {
            "name": "--foo",
            "required": True,
        }, {
            "name": "-f",
            "required": False,
            "env_var": "LETTER_F",
        }
    ]
})

print "get_all=", cfgur.get_all()


print "test   =", cfgur.get("test")
# This will never exist, but will just return None
print "test2  =", cfgur.get("test2")
# This will fail with argparse if --foo or FOO="" do not exist
print "foo    =", cfgur.get("foo")
# This will fail with config.get if -f or LETTER_F="" do not exist
print "f      =", cfgur.get("f", True)
