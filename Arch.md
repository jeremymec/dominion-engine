# Dominion

Dominion is a game which has some stuff.



## Game Setup

### Games have

Players
A set of cards that can be bought
A list of events that have happened
A stack of events

### Players have

Name
Deck of cards
Hand of cards
Discard pile of cards
Victory points

## Effects

Most things in dominion are an effect. There are two types of effects. Those that auto-resolve, and those that need player selection to resolve.

### Effects have

|    Field    | Description                                                  |
| :---------: | ------------------------------------------------------------ |
|   Player    | The assigned/target player                                   |
|    Type     | Type of Effect (e.g. discard, draw, trash, acquire)          |
|    Scope    | List of cards the effect is restricted to (if applicable)    |
|   Amount    | Amount of things the effect applies to / acts on (if applicable) |
| AutoResolve | If the effect requires manual intervention                   |
|  Mandatory  | If not auto resolved, can the effect be skipped              |
| Description | If not auto resolved, flavor text explaining the move        |

### Examples

*At the start of a players turn, a 'Draw 5' effect is added*

**Effect**
  Player: Player-ID
  Type: Draw
  Scope: N/A
  Amount: 5
  AutoResolve: Yes
  Description: Omitted



*A player is forced to discard a curse as a result of an action card*

**Effect**
  Player:  Player-ID
  Type: Discard
  Scope: Curse
  Amount: 1
  AutoResolve: No
  Mandatory: Yes
  Description: Omitted



## Cards

Cards aren't effects, but they can be associated with effects that trigger when they are played.

### Cards Have

|    Field    | Description                                              |
| :---------: | -------------------------------------------------------- |
|    Name     | The name of the card                                     |
|    Type     | Treasure \| Victory \| Action                            |
|    Cost     | Number                                                   |
|   Effects   | A list of effects to be executed when the card is played |
| Description | Text on the card                                         |

### 

## Events

Events are used for recording what happens in the game. They are emitted by effects (and possibly by the game itself) and should be logged to the user through the client.



## Game Loop

The game will expose an interface for the client to call certain 'actions'.

Examples of this could be
**Action**
  Type: Buy Card
  Cards: <Card-Name>
  Player: <Player-ID>

or

**Action**
  Type: Discard Cards
  Cards: [<Card1>, <Card2>]
  Player: <Player-ID>

These actions will either be accepted or rejected based on factors like the current turn, amount of money the player has, and the games internal state (phase?)



## Sample Game Timeline



### Setup Phase

Game is started with initial parameters

- List of players and their names
- List of cards available in the game


Then starting cards are distributed to each player

- Effect to put coppers in deck of first player put on effect stack
  **Effect**
    Player: <First-Player-ID>
    Type: Acquire
    Amount: 7
    AutoResolve: True  
- This effect will emit an event that seven coppers have been placed in the first players deck
- *Effects are put on the stack for the other cards the player needs, as well as the other players.* 
- The effects are resolved and the effect stack is cleared.



Decks and shuffled and cards drawn

- Effects to shuffle decks and draw cards for each player are placed on the stack and resolved.



It's player 1's turn, and it's the action phase

- Effect for player one to play actions is pushed on the effect stack
  **Effect**
    Player: <First-Player-ID>
    Type: Play
    Scope: Actions
    Amount: 1
    AutoResolve: False
    Mandatory: No
    Description: You may play actions
- The effect is consumed, but not resolved.
- The client either calls PlayCard, consuming the action effect or calls SkipResolve seeing as the effect isn't mandatory.
  ***Somehow the game needs to know how effects are resolved.***
- The effect is resolved. 

It's now the buy phase of player 1s turn.

- Effect for player one to buy cards is pushed on the stack
  **Effect**  Player: <First-Player-ID>
    Type: Buy
    Scope: All
    Amount: 1
    AutoResolve: False
    Mandatory: No
    Description: You may buy cards
- It is worth noting that during this phase the player may play treasures from their hand to gain money
  ***Somehow the game needs to know that this is allowed***.
- The client can call PlayCard on Treasure cards, and can call BuyCard once. They can also call SkipResolve.
- The effect is resolved.

Now the effect stack is empty the game runner pushes Effect for player two to buy cards and etc...





















