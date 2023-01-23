# Google API Notes

## Volume

A volume represents the data that Google Books hosts about a book or magazine. It is the primary resource in the Books API. All other resources in this API either contain or annotate a volume.

## Bookshelf
A bookshelf is a collection of volumes. Google Books provides a set of predefined bookshelves for each user, some of which are completely managed by the user, some of which are automatically filled in based on user's activity, and some of which are mixed. Users can create, modify or delete other bookshelves, which are always filled with volumes manually. Bookshelves can be made private or public by the user.

**Note**: Creating and deleting bookshelves as well as modifying privacy settings on bookshelves can currently only be done through the Google Books site.

## Review
A review of a volume is a combination of a star rating and/or text. A user can submit one review per volume. Reviews are also available from outside sources and are attributed appropriately.

## Reading Position

A reading position indicates the last read position in a volume for a user. A user can only have one reading position per volume. If the user has not opened that volume before, then the reading position does not exist. The reading position can store detailed position information down to the resolution of a word. This information is always private to the user.
