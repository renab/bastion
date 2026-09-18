# Executive Brief UI Reference

![Executive Brief consolidated chain workspace](executive-brief-workspace.png)

## Product purpose and concept

Executive Brief is Bastion’s default **map-first operational cockpit**.

It is the consolidated live chain-and-opportunity workspace, not a summary dashboard paired with a separate Chain page.

Its purpose is to answer, at a glance:

- what the live topology is;
- where the value is in the current chain;
- which systems matter most;
- how much opportunity exists in total;
- how much is capability-covered;
- how much is actually actionable now;
- which systems or connections require intervention;
- which characters are currently relevant;
- what canonical domain object should be opened next.

The map is not decorative.

It is a real interactive topology graph.

One real system is represented by one graph node.  
One real wormhole connection is represented by one graph edge.

Visual layout may change for readability, but topology truth must not.

Supporting surfaces such as Attention, active characters, search, legend, filters, and system inspection exist to support the map rather than displace it.

---

# Core product distinction

Nexum supplies topology.

**Bastion evaluates that topology.**

The Executive Brief must preserve Bastion’s value-add over a plain wormhole map:

- visual valuation of the chain;
- system-by-system opportunity grading;
- capability coverage;
- actionability;
- explainable opportunity composition;
- operational intervention context.

A graph that only shows system class/security and wormhole connections is insufficient, even if the graph behavior itself is excellent.

The map must visually and numerically answer:

> Where is the value in this chain, how much of it can we exploit, and what can we act on right now?

---

# Primary page structure

The Executive Brief contains:

1. global operational search;
2. compact active-character strip;
3. bounded Attention rail;
4. dominant live topology graph;
5. opportunity metric controls;
6. Relative / Fixed normalization control;
7. category / overlay filters;
8. selected-system contextual inspector;
9. optional selected-connection inspector;
10. map legend;
11. Operations HQ and Market HQ context.

The core operating picture should fit within the intended desktop viewport without requiring vertical page scrolling.

---

# Interactive topology graph

## Graph truth

The chain map must be implemented as an actual node-edge graph.

Each node represents one real system.

Each edge represents one real wormhole connection.

Moving a node changes only presentation.

It does not change:

- connection ownership;
- topology;
- source/target systems;
- wormhole facts.

## Anchored edges

Every connection edge must remain attached to its source and target nodes.

When a node moves:

- connected edge endpoints move with it continuously;
- edge routing updates in real time;
- wormhole labels remain attached to the edge;
- mass/EOL/attention markers remain attached to the edge.

Detached, floating, or static line segments are invalid.

A graph where moved nodes separate from their connection lines is broken behavior.

## Node drag

Dragging a node should:

- move that node only;
- update attached edges continuously;
- preserve all graph relationships;
- preserve filters;
- preserve selected opportunity metric;
- preserve selection state.

Dragging a node must not accidentally pan the canvas.

## Canvas pan and zoom

Normal interaction should distinguish:

- drag empty canvas → pan;
- drag node → move node;
- click node → select;
- click edge → inspect connection;
- wheel / pinch → zoom.

The map should support:

- smooth pan;
- zoom;
- fit topology;
- recenter on Operations HQ;
- reset view;
- auto-layout.

## Layout persistence

Manual placement should persist through ordinary interaction.

Changing:

- selection;
- filters;
- active opportunity metric;
- Relative / Fixed mode;
- open drawer;
- closed drawer

must not reset the map layout.

Where practical, operator-adjusted layout should persist across sessions.

Newly discovered systems should be placed sensibly without unnecessarily destroying the existing arrangement.

## Automatic layout

Automatic layout may be used to:

- organize a new chain;
- recover from an unreadable layout;
- fit topology into the viewport.

Manual placement can override automatic layout.

Automatic layout is a presentation tool and never changes topology truth.

## Live topology updates

Chain changes should update incrementally where practical.

Examples:

- new system → add node;
- new wormhole → add edge;
- collapsed connection → remove/update edge;
- changed mass/EOL state → update edge;
- changed system metadata → update node.

Avoid rebuilding the entire graph in a way that destroys operator context or manual placement.

## Map implementation expectation

Use a mature maintained graph/canvas library suitable for:

- node dragging;
- anchored edges;
- edge routing;
- pan;
- zoom;
- selection;
- incremental graph updates;
- layout algorithms.

Do not implement the production map as independently positioned HTML elements plus disconnected line graphics.

---

# System-node design

Bastion should use **compact information-rich system nodes**, visually inspired by the useful density of Nexum’s system cards without reimplementing Nexum itself.

The default node should not be limited to an anonymous colored circle when useful system context can be shown directly.

At normal working zoom, a node may expose:

- system name;
- class / security type;
- Operations HQ / home marker where relevant;
- selected opportunity/value grade;
- selected opportunity/value amount;
- compact static / connection summary where useful;
- attention marker;
- opportunity marker.

## Node shape

Prefer a compact rectangular, rounded-rect, or hybrid card node with clear graph connection anchors/ports rather than pure circles as the default representation.

Operations HQ may use a stronger visual treatment while preserving the same graph semantics.

## Progressive density

Node contents should adapt to zoom level.

At distant zoom:

- simplify text;
- preserve system identity;
- preserve class border;
- preserve opportunity/value heat signal.

At normal / near zoom:

- expose compact metadata;
- expose static / connection summary;
- expose value grade / amount where useful.

Do not allow text density to make the topology unreadable.

---

# Nexum design boundary

Nexum is the authoritative topology source and a useful interaction / visual reference.

Bastion may take inspiration from Nexum for:

- compact system-card nodes;
- visible system identity and class/security;
- compact static / connection context;
- anchored graph edges;
- readable branching;
- operator-friendly chain manipulation;
- edge-bound labels and connection-state markers.

Bastion should not recreate:

- Nexum signature editing;
- anomaly editing;
- structure editing;
- its full topology-management sidebar;
- Nexum-specific administrative controls;
- its exact node schema or visual styling;
- a competing standalone mapping product.

Bastion consumes Nexum topology and adds its own operational semantics:

- opportunity valuation;
- capability coverage;
- actionability;
- Attention;
- cross-domain handoff;
- Operations HQ context.

---

# Opportunity value model

The map must support at least three distinct opportunity metrics.

These are not interchangeable.

## Total Potential

Represents all evaluated opportunity value currently present in the system, regardless of whether Bastion believes Naffin Enterprises can currently exploit it.

Answers:

> How much raw opportunity exists here?

## Capability-Covered Potential

Represents the portion of opportunity value that current connected characters, doctrines, ships, skills, and capabilities can execute in principle.

Answers:

> How much of this opportunity are we actually equipped to exploit?

## Actionable Potential

Represents capability-covered value further constrained by immediate operational reality.

Possible constraints include:

- character availability;
- doctrine availability;
- logistics;
- route practicality;
- current blockers;
- freshness;
- risk state;
- current operational commitments;
- other execution constraints.

Answers:

> What can we realistically act on now?

The UI must never collapse Total Potential, Capability-Covered Potential, and Actionable Potential into a single unexplained score or interchangeable count.

---

# Opportunity metric controls

Provide an explicit metric selector such as:

- **Total Potential**
- **Capability-Covered**
- **Actionable**

The currently active metric must be obvious.

Changing the metric changes:

- value amount;
- value grade;
- node interior fill;
- node glow;
- valuation number / grade badge;
- inspector explanation.

It does not change:

- topology;
- system class;
- connection truth.

Metric selection should persist through ordinary map interaction and inspector use.

---

# Relative vs Fixed grading

Relative / Fixed is a separate concept from the selected opportunity metric.

## Relative

Relative grading compares systems against the current visible / current operating set.

Useful for answering:

> Which systems are best relative to this chain right now?

## Fixed

Fixed grading uses stable Bastion-defined thresholds or normalization.

Useful for answering:

> Is this system objectively strong or weak against a stable reference?

Relative / Fixed changes the grading interpretation only.

It must not change:

- topology;
- system class;
- metric selection.

---

# Opportunity value grading

The WN8/WNX-inspired grading scale is a required **visible semantic channel**, not subtle decoration.

Conceptual order:

**very poor → poor → below average → average → good → very good → excellent → exceptional**

Conceptual color progression:

**red → orange → yellow → green → teal/cyan → blue → purple**

Unknown or unmeasured state must remain neutral/dim and must never be represented as red/bad.

Do not reuse WN8 numeric thresholds literally.

Bastion must define explainable thresholds or normalization appropriate to EVE opportunity value.

---

# Required value encoding on the map

At normal zoom, the active value grade must be immediately visible.

Do not rely on a subtle glow alone.

Use:

- **node interior / fill** for the active value grade;
- **node glow** to reinforce the same grade;
- **valuation amount and/or grade badge** colored to match the active valuation grade;
- value amount / grade in the selected-system inspector;
- legend showing the full grade ramp and active metric.

The valuation color applies only to valuation-specific elements.

It must not replace:

- system-class border color;
- system-class text color;
- selection state;
- alert state.

## Redundant valuation cues

A node should communicate valuation through multiple coordinated cues:

- fill/tint;
- glow;
- valuation amount color;
- optional grade badge / label.

This redundancy is intentional.

It improves rapid visual recognition and protects meaning when one visual cue is weak or obscured.

---

# System class / security encoding

System class / security is a separate semantic channel from valuation.

## Border / stroke

The node border answers:

> What kind of system is this?

Use the established Nexum class/security palette for:

- HS
- LS
- NS
- C1
- C2
- C3
- C4
- C5
- C6
- supported special / unknown classes

Border color must carry system type only.

It must never change with valuation grade.

## Class / security text

The class/security label inside the node should use the same semantic class/system-type color as the node border.

Examples:

- `HS`
- `NS`
- `C2`
- `C5`

This reinforces the class signal without coloring the entire node typography.

---

# Targeted semantic text color

Node typography should use semantic color selectively.

## Class / security

Color using the corresponding system-class / security color.

## Valuation amount / grade

Color using the active valuation-grade color.

Examples:

- `620M ISK`
- `Excellent`
- `A`
- other compact grade representation

## Neutral text

Keep ordinary information high-contrast neutral, normally white or light gray.

This includes:

- system name;
- statics labels;
- connection labels inside the node;
- ordinary metadata;
- supporting counts;
- general descriptive text.

Do not globally tint node text by system type or valuation.

Semantic color should reinforce meaning only where the text itself carries that meaning.

---

# Accessibility and readability

Color must not be the sole carrier of class or valuation.

System type remains explicit in text such as:

- `C3`
- `HS`
- `NS`

Valuation should also remain explicit through:

- numeric amount;
- grade badge;
- grade label where useful.

The interior valuation tint must remain dark enough to maintain readable text contrast.

The border must remain visually distinguishable from the fill/glow even when class color and valuation color are similar.

If necessary, the final UI/UX design may use:

- a neutral separator;
- inner/outer stroke;
- slight spacing between fill and border;
- controlled opacity differences

to keep the semantic channels distinct.

---

# Selection state

Selection is a separate interaction channel.

Selected/focused state should use something such as:

- a neutral/high-contrast selection ring;
- thicker outer focus outline;
- explicit selected marker.

Do not reuse:

- valuation glow;
- class border color;
- alert color

as the sole selected-state indicator.

---

# Mockup quality gate for semantic color

Executive Brief mockups are not acceptable unless both system class and valuation are simultaneously legible.

A valid node must make it possible to distinguish:

1. **what type/class the system is**, and
2. **how valuable it is under the selected metric**.

The reference image should deliberately include combinations where these colors differ strongly.

Example:

A C3 system may have:

- C3 class-colored border;
- `C3` text in the same class color;
- purple valuation interior/glow;
- purple valuation amount / `Exceptional` badge;
- system name and ordinary metadata in white.

The renderer must not collapse the class border into the valuation color.

The renderer must not leave the valuation interior effectively neutral.

---

# Mockup quality gate for value grading

The reference image should deliberately include multiple systems occupying visibly different grades across the valuation ramp.

For example:

- red;
- orange;
- yellow;
- green;
- teal/cyan;
- blue;
- purple.

A mockup where every node is effectively the same dark fill with only faint differences fails this requirement.

The viewer should be able to identify high-value and low-value branches before opening every node.

---

# Edge design

Connection edges are first-class selectable graph objects.

They may expose:

- wormhole type;
- connection state;
- mass state;
- EOL state;
- freshness;
- attention marker.

Labels belong to the edge and move with it.

## Directionality

Do not use arrows purely as decoration.

Only communicate direction if the underlying wormhole semantics actually require it.

Otherwise represent the relationship as a connection rather than implying false directional meaning.

## Edge interaction

Connections should have a usable selectable hit target even if the visible line remains thin.

Selecting a connection may open a lightweight connection inspector without losing map context.

---

# Selected-system inspector

Selecting a node opens a contextual right-side inspector.

This inspector should answer:

- what is this system?
- what is known here?
- how much value exists here?
- how much is capability-covered?
- how much is actionable?
- why did it receive this grade?
- what opportunities contribute most?
- what blockers suppress Actionable value?
- what should I open next?

Useful sections may include:

- system identity;
- class/security;
- distance / relation to Operations HQ;
- scan freshness;
- statics;
- current connections;
- local activity;
- local sites / opportunities;
- active opportunity metric amount;
- value grade;
- top contributing opportunities;
- capability coverage;
- actionable blockers;
- freshness / confidence.

Actions include:

- **Open Source**
- **View Full Page**

Opening and closing the inspector must preserve:

- node placement;
- zoom;
- pan;
- filters;
- selected opportunity metric;
- Relative / Fixed mode;
- selection state.

---

# Connection inspector

Selecting an edge may open a lightweight contextual inspector containing:

- source system;
- destination system;
- wormhole type;
- mass state;
- EOL state;
- observation freshness;
- associated Attention item if present.

Deeper topology management belongs to Nexum where appropriate.

---

# Active-character strip

The top-right character strip is compact operational context, not character management.

Its purpose is to answer:

> Which characters are currently active or operationally relevant?

It may show:

- official portrait;
- full canonical name;
- compact location;
- ship;
- current task/status where useful.

Selecting a character hands off to Accounts / Characters.

Character management, ESI authorization, and training detail do not belong in the Executive Brief.

---

# Attention rail

Attention is an intervention queue, not a generic event ticker.

The compact Brief surface should show only:

- unresolved high-priority intervention;
- meaningful recently completed events.

Examples:

- critical wormhole mass;
- PI intervention due;
- important market lifecycle event;
- hostile activity;
- meaningful training milestone;
- logistics / procurement blocker.

Attention lifecycle:

## Completed / informational
May be acknowledged / dismissed.

## Unresolved operational work
May be deferred / snoozed.

## Source-state resolution
Derived alerts resolve automatically when the underlying condition is no longer true.

Attention should aggregate similar events when that improves signal.

---

# Legend

The legend must visibly explain all independent semantic channels.

It should show:

## System Class / Security
**Border + class label**

Examples:
- HS
- LS
- NS
- C1-C6

## Opportunity Value
**Interior fill + glow + valuation amount / grade**

Show:
- active metric;
- full grade ramp;
- unknown state.

## Connection State
**Edge treatment**

Examples:
- known;
- unstable / EOL;
- unknown.

## Special markers

Examples:
- Operations HQ;
- opportunity;
- Attention;
- other supported states.

Changing opportunity metric or Relative / Fixed mode must never alter the system-class border.

---

# Important states

| Surface | State | Required behavior |
| --- | --- | --- |
| Map | Loading | Show loading state without fake topology |
| Map | No active chain | Purposeful empty state explaining no live topology is currently available |
| Map | Stale topology | Keep topology visible if useful but clearly mark degraded freshness |
| Map | Source disconnected | Explicitly identify unavailable topology source; never render unknown as empty |
| Map | New topology discovered | Add incrementally without destroying layout where practical |
| System inspector | No matching opportunities | Say none match active filters; do not imply the system itself is irrelevant |
| System inspector | Stale evaluation | Show degraded freshness/confidence |
| System inspector | Capability gap | Show value exists but current capability does not cover it |
| System inspector | Actionability blocker | Show what suppresses Actionable value |
| Edge | Unknown / incomplete state | Render unknown state explicitly |

---

# Representative workflow

1. open Executive Brief;
2. review Attention and active characters;
3. inspect live topology;
4. choose opportunity metric;
5. choose Relative / Fixed grading;
6. apply category filters if useful;
7. visually identify high-value and low-value branches;
8. pan / zoom / rearrange nodes if useful;
9. select a system;
10. inspect value amount, grade, contributors, capability coverage, and blockers;
11. optionally inspect a connection;
12. open the owning domain / source object;
13. perform the action there;
14. return to the preserved Brief map context.

Navigation is traversal-aware.

Example:

`Executive Brief > J123456 > Gas Site > Harvest Doctrine`

Back should return to the actual map state that launched the drill-down.

---

# Must not do

Executive Brief must not:

- create a second Chain / Opportunities page;
- reduce Bastion to a topology viewer;
- treat the graph as decorative;
- draw connections independently of nodes;
- allow moved nodes to detach from their edges;
- rebuild/reset layout on ordinary interaction;
- imply false edge direction;
- invent spatial geography;
- let supporting panels push the map below the desktop fold;
- use system-type color and opportunity-value color for the same semantic channel;
- color the class border using valuation grade;
- leave the valuation interior effectively neutral;
- globally tint ordinary node text;
- make value grading so subtle that high/low systems are not obvious;
- collapse Total Potential, Capability-Covered, and Actionable into one unexplained score;
- turn nodes into opaque circles that require a drawer for every basic fact;
- become a Nexum clone;
- duplicate canonical domain-management interfaces inside the inspector;
- become a generic KPI dashboard.

---

# Visual-generation brief

Render a dense 16:9 Bastion **Executive Brief** operational workspace.

The map must be the dominant element.

Use a true node-edge graph visual with:

- compact Nexum-inspired Bastion system cards rather than simple circles;
- visible system name;
- visible class/security label;
- Operations HQ emphasized;
- real connection edges visibly anchored to node boundaries / ports;
- edge labels attached to the corresponding edges;
- compact mass / EOL / Attention markers where relevant.

Each system node must visibly carry **two independent semantic color channels**:

## Class / system type
- thin crisp node border uses system-class/security color;
- class/security text uses the same system-class/security color;
- border color never changes with valuation.

## Opportunity valuation
- node interior is visibly tinted by valuation grade;
- soft outer glow uses the same valuation-grade color;
- valuation amount and/or grade badge uses the valuation-grade color;
- valuation color never replaces the system-class border.

All other node text should remain white / high-contrast neutral.

The mockup must deliberately include several nodes with clearly different combinations of:

- class border colors; and
- valuation fill/glow colors.

At least several valuation grades should be visibly represented:

- red;
- orange;
- yellow;
- green;
- teal/cyan;
- blue;
- purple.

Also include:

- explicit metric selector:
  - Total Potential
  - Capability-Covered
  - Actionable
- Relative / Fixed control;
- category filters;
- visible legend explaining:
  - border + class text = system class/security;
  - fill + glow + valuation text = opportunity value;
- compact active-character strip;
- compact Attention rail;
- right-side selected-system inspector showing:
  - active metric amount;
  - value grade;
  - top contributing opportunities;
  - capability coverage;
  - actionable blockers;
  - freshness/confidence;
- optional selected-connection state.

The visual should imply that:

- nodes can be dragged;
- edges remain attached while nodes move;
- canvas can pan / zoom;
- layout can be fitted / reset / auto-arranged.

Avoid:

- circle-only node presentation;
- detached connection graphics;
- decorative arrows;
- border colors that match valuation instead of class;
- neutral/dark interiors that fail to show valuation;
- globally colored node typography;
- generic dashboard KPI walls;
- a separate Chain nav destination;
- a tiny map surrounded by cards;
- topology-only presentation with no Bastion valuation layer.

---

# Interpretation boundary

A future UI/UX designer may change:

- exact node-card dimensions;
- field density;
- edge curvature;
- anchor positioning;
- layout algorithm;
- control placement;
- inspector proportions;
- progressive zoom behavior;
- map background treatment;
- exact grade-badge design;
- exact method used to preserve border/fill contrast.

The following must be preserved:

- actual interactive graph semantics;
- one real system per node;
- one real connection per edge;
- anchored edges;
- node dragging without topology mutation;
- persistent operator layout/context;
- map dominance;
- Nexum-inspired information density without cloning Nexum;
- explicit Bastion opportunity/value layer;
- Total Potential / Capability-Covered / Actionable distinction;
- Relative / Fixed distinction;
- visible WN8/WNX-inspired grade ramp;
- class border + class text semantic channel;
- valuation fill/glow + valuation text semantic channel;
- neutral ordinary typography;
- explainable selected-system valuation;
- Attention lifecycle;
- compact active-character context;
- Operations HQ vs Market HQ distinction;
- context-preserving cross-domain handoff.

---

# Authoritative design sources

Relevant current sources include:

- current `wormlife-local-operations-console-v1`
- current `bastion-chain-map-interaction-v1`
- current `bastion-attention-model-v1`
- current `bastion-cross-domain-navigation-v1`
- relevant Executive Brief sections in:
  - `wormlife-trial/05 Planning/Outbound Flight - Bastion Design Notes.md`
  - `wormlife-trial/05 Planning/Outbound Flight - Nirauan Design Notes.md`

Resolve current Galaxy records at implementation time rather than relying indefinitely on copied UUIDs.

Current source hierarchy:

1. current Galaxy structured decisions;
2. current Bastion Design Notes;
3. non-superseded Nirauan design;
4. approved visual references;
5. historical prototype.

The visual reference is approved UI/UX direction, not a pixel contract.