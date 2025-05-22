# 1. Why is Agent a Python dataclass?

# Python’s @dataclass is syntactic sugar with powerful benefits:

# No more boilerplate __init__

# Auto-type checking & default values

# Easy debugging with clear representations

# Serialization support (think logging, state saving)

# Logic Check: AI agents often have lots of attributes (name, instructions, tools). @dataclass makes them clean and readable.

# 2. Why are system prompts stored as instructions in the Agent—and why are they callable?

# Prompts = Brain Instructions 🧠

# Storing them in Agent keeps identity and behavior bound together.

# Making them callables allows context-aware behavior (like changing tone, language, or domain dynamically).

# Fun Fact: You can create bilingual or mood-sensitive agents with dynamic instructions. Try an agent that speaks French in the morning and English at night! 🥖☕

# 3. Why is Runner.run() a @classmethod, and why does it take user input?

# The user prompt changes with each interaction—hence passed at runtime.

# @classmethod means no object instantiation—perfect for stateless execution and testing.

# Logic Tip: This design pattern enables cleaner CLI tools, APIs, and script-based execution.

# 4. What is the Runner?

# The Runner is your execution engine. It:

# Accepts input

# Applies memory, tools, and instructions

# Invokes the LLM

# Returns a structured, intelligent response

# Runner = the agent’s chauffeur—it drives the conversation safely and smoothly. 🏎️

# 5. What are Generic[T] and TContext?

# Python generics allow type-safe reusability.

# TContext = generic context type

# Guarantees agents can safely use and manipulate custom memory models

# Fun Fact: Generics are like blueprints—you define once, and reuse safely across any project with different materials (types).

# 🌐 Use Cases — Not Just Chatbots

# Here’s where the SDK shines:

# 📈 Business automation: Agents for scheduling, data entry, email generation

# 🎓 Education: Tutoring bots, quiz generators, lesson planners

# 🛒 E-Commerce: Order tracker, recommendation engine, support agent

# 🧠 Research: Citation managers, summarizers, document crawlers

# Fun Fact: You can even create agents that teach other agents how to behave. Meta!
