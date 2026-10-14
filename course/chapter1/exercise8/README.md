# Stop Words

Now that we have a list of tokens, we need to decide which ones are _actually useful_ for search. Not all tokens are created equal...

## Examples of High-Value Tokens

- bear
- panda
- london
- protector

## Examples of Low-Value Tokens

- a
- the
- is
- of
- in

These are examples of [stop words](https://en.wikipedia.org/wiki/Stop_word): common words that usually don't add much meaning. In short, _we're going to remove them_.

## Why Remove Stop Words?

Our goal is to match words from the user's input to words in our dataset. If we don't remove stop words, we can get some pretty misleading results. Here's an example:

**User query:** "the bear"

**Results:**

- "Jungle Bear": matches "bear".
- "The Terminator": matches "the".

**Oof!** Both movies match, but "Jungle Bear" is clearly more relevant. "The Terminator" matches only on a low-value stop word.

## Assignment

**Remove stop word tokens** from both the user query and the title tokens.

1. [ ] Create a new `data/stopwords.txt` file and paste the words at the end of this page into it.
2. [ ] Read the stop words from the file and store them in a list.
   - [`.read()`](https://docs.python.org/3/library/io.html#io.TextIOBase.read) the file
   - [`.splitlines()`](https://docs.python.org/3/library/stdtypes.html#str.splitlines) to split it into a list of words
3. [ ] Preprocess the stop words the same way you preprocess the user query and title text.
   - For example, `aren't` should become `arent` before you compare tokens against it!
4. [ ] Load and preprocess the stop words once, then reuse that list whenever you filter tokens.
5. [ ] Filter any stop words out of both the user query tokens and title tokens before matching.

**Run and submit** the CLI tests.

## Stopword List

```text
a
about
above
after
again
against
ain
all
am
an
and
any
are
aren
aren't
as
at
be
because
been
before
being
below
between
both
but
by
can
couldn
couldn't
d
did
didn
didn't
do
does
doesn
doesn't
doing
don
don't
down
during
each
few
for
from
further
had
hadn
hadn't
has
hasn
hasn't
have
haven
haven't
having
he
he'd
he'll
he's
her
here
hers
herself
him
himself
his
how
i
i'd
i'll
i'm
i've
if
in
into
is
isn
isn't
it
it'd
it'll
it's
its
itself
just
ll
m
ma
me
mightn
mightn't
more
most
mustn
mustn't
my
myself
needn
needn't
no
nor
not
now
o
of
off
on
once
only
or
other
our
ours
ourselves
out
over
own
re
s
same
shan
shan't
she
she'd
she'll
she's
should
should've
shouldn
shouldn't
so
some
such
t
than
that
that'll
the
their
theirs
them
themselves
then
there
these
they
they'd
they'll
they're
they've
this
those
through
to
too
under
until
up
ve
very
was
wasn
wasn't
we
we'd
we'll
we're
we've
were
weren
weren't
what
when
where
which
while
who
whom
why
will
with
won
won't
wouldn
wouldn't
y
you
you'd
you'll
you're
you've
your
yours
yourself
yourselves
```
