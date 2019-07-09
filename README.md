# eliza
A simple replica of ELIZA. This implementation essentially prioritizes certain keywords/phrases as being the most signifcant drivers of the response type. More info [here](https://en.wikipedia.org/wiki/ELIZA).

## Usage
To try it out, download the package and run `python eliza` from the command line. You can also import the eliza_replica.py module:
```python
from eliza import eliza_replica
# for some input, txt
response = eliza_replica.response(txt)
```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
