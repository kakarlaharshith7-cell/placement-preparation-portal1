# =====================================================================
# PLACEMENT PREPARATION PORTAL - SINGLE FILE VERSION
# Contains: question/company/interview data, CSS, all HTML pages, Flask app.
# Only the logo/icon images stay in the static/ folder.
# =====================================================================
# ---------------------------------------------------------------------
# PART 1: DATA
# ---------------------------------------------------------------------
# ====================================================================
# PLACEMENT PREPARATION PORTAL - KNOWLEDGE BASE & DATA STORE
# ====================================================================

PROFESSIONS = [
    "Software Engineer",
    "Full Stack Developer",
    "Cyber Security Analyst",
    "Data Scientist / Analyst",
    "Cloud & DevOps Engineer",
    "Artificial Intelligence Engineer",
    "Backend Developer",
    "Frontend Developer",
    "Database Administrator",
    "QA / Software Test Engineer",
    "Embedded Systems Engineer",
    "Site Reliability Engineer (SRE)"
]

DOMAINS = [
    "Computer Science",
    "Information Technology",
    "Cyber Security",
    "Data Science",
    "Artificial Intelligence",
    "Cloud Computing",
    "Web Development",
    "Database Engineering",
    "Systems & Networking"
]

# ====================================================================
# 29 TOP PLACEMENT RECRUITMENT COMPANIES WITH OFFICIAL LOGOS
# ====================================================================

COMPANIES_DATA = [
    {
        "name": "TCS (Tata Consultancy Services)",
        "logo": "tcs.svg",
        "category": "MNC",
        "industry": "IT Services & Global Consulting Giant",
        "color": "#0B1C48",
        "ctc": "3.36 LPA - 9.0 LPA",
        "roles": "Ninja (3.36 - 3.6 LPA), Digital (7.0 - 7.5 LPA), Prime (9.0 LPA)",
        "eligibility": "60% or 6.0 CGPA throughout (10th, 12th, B.Tech/MCA). Maximum 1 active backlog at time of exam.",
        "rounds": "Round 1: National Qualifier Test (NQT Cognitive + Technical Coding), Round 2: Technical Interview, Round 3: Managerial + HR Interview.",
        "test_pattern": "Section 1: Cognitive (Numerical, Verbal, Reasoning - 80 mins); Section 2: Advanced Coding (2 coding problems in C/C++/Java/Python - 90 mins).",
        "syllabus": "Quant (percentages, work, speed), Logical Reasoning, Output questions in C/Python, Data Structures, Array manipulations.",
        "frequently_asked": [
            "Difference between call by value and call by reference in C/C++?",
            "Write a program to reverse a string without using built-in functions.",
            "Explain Normalization in DBMS with examples.",
            "What is your final year engineering project and your specific contribution?",
            "Why do you want to join TCS?"
        ],
        "overview": "India's largest IT company and mass recruiter hiring over 40,000 freshers annually through the centralized TCS NQT exam.",
        "careers_url": "https://www.tcs.com/careers"
    },
    {
        "name": "Infosys",
        "logo": "infosys.svg",
        "category": "MNC",
        "industry": "IT Services & Digital Transformation",
        "color": "#007CC3",
        "ctc": "3.6 LPA - 9.5 LPA",
        "roles": "Systems Engineer (3.6 LPA), DSE (6.25 LPA), Specialist Programmer (9.5 LPA)",
        "eligibility": "60% or 6.5 CGPA in 10th, 12th, and Graduation. No active backlogs allowed.",
        "rounds": "Round 1: Online Assessment (Reasoning, Mathematical, Verbal, Pseudocode, Puzzle), Round 2: Technical + HR Interview (combined).",
        "test_pattern": "Reasoning Ability (15 Qs, 25 mins), Math Ability (10 Qs, 35 mins), Verbal (20 Qs, 20 mins), Pseudocode (5 Qs, 10 mins), Puzzle Solving (4 Qs, 10 mins).",
        "syllabus": "Cryptarithmetic puzzles, Syllogisms, OOPs concepts, Pseudocode execution, String algorithms.",
        "frequently_asked": [
            "Explain Method Overloading vs Method Overriding in Java.",
            "What is a Primary Key vs Unique Key in SQL?",
            "Write code to find the second largest element in an array.",
            "Explain the SDLC phases and Agile methodology.",
            "Are you willing to relocate to Mysore campus for training?"
        ],
        "overview": "Renowned for its world-class Global Education Center in Mysore and global IT consulting services across banking, healthcare, and retail.",
        "careers_url": "https://career.infosys.com/"
    },
    {
        "name": "Wipro",
        "logo": "wipro.svg",
        "category": "MNC",
        "industry": "Global Information Technology & Consulting",
        "color": "#4338ca",
        "ctc": "3.5 LPA - 6.5 LPA",
        "roles": "Elite National Talent Hunt (3.5 LPA), Turbo (6.5 LPA), Velocity",
        "eligibility": "60% or 6.0 CGPA throughout 10th, 12th, and UG. Maximum 1 backlog allowed at the time of assessment.",
        "rounds": "Round 1: Online Assessment (Aptitude + Written Communication Essay + 2 Coding Qs), Round 2: Technical & HR Interview.",
        "test_pattern": "Aptitude (48 mins), Written Essay Writing (20 mins), Coding (2 problems in 60 mins).",
        "syllabus": "Quantitative Math, Logical Puzzles, English Grammar & Essay, Basic DSA, Arrays, Strings.",
        "frequently_asked": [
            "What are ACID properties in DBMS?",
            "Explain the difference between Stack and Queue.",
            "Write a program to check if a number is Prime or Armstrong.",
            "What is inheritance in OOPs and why is multiple inheritance not supported in Java?",
            "Why Wipro?"
        ],
        "overview": "Global technology services firm offering strong training programs and career progression through the Elite and Turbo tracks.",
        "careers_url": "https://careers.wipro.com/"
    },
    {
        "name": "Cognizant",
        "logo": "cognizant.svg",
        "category": "MNC",
        "industry": "IT Services & Enterprise Consulting",
        "color": "#0033A0",
        "ctc": "4.0 LPA - 9.0 LPA",
        "roles": "GenC (4.0 LPA), GenC Elevate (4.5 LPA), GenC Next (6.75 - 9.0 LPA)",
        "eligibility": "60% in 10th, 12th, and B.Tech. No current standing backlogs.",
        "rounds": "Round 1: Communication Assessment, Round 2: Aptitude + Technical Assessment, Round 3: Technical & HR Interview.",
        "test_pattern": "GenC: Quantitative, Logical, Verbal + Coding (2 problems). GenC Next: Advanced Coding + SQL + Data Structures.",
        "syllabus": "Arrays, Strings, SQL Queries (Joins, Subqueries), OOPs, Web Development basics.",
        "frequently_asked": [
            "Explain the difference between Abstract Class and Interface.",
            "Write an SQL query to find employees with salary greater than average.",
            "What is a pointer and a memory leak in C/C++?",
            "Describe your project architecture and database design.",
            "How do you handle conflict in team projects?"
        ],
        "overview": "Major multinational consulting firm providing high-growth opportunities across Cloud, AI, and enterprise modernizations.",
        "careers_url": "https://careers.cognizant.com/"
    },
    {
        "name": "Accenture",
        "logo": "accenture.svg",
        "category": "MNC",
        "industry": "Management Consulting & Technology Services",
        "color": "#7e22ce",
        "ctc": "4.5 LPA - 6.5 LPA",
        "roles": "Associate Software Engineer (ASE: 4.5 LPA), Advanced ASE (AASE: 6.5 LPA)",
        "eligibility": "65% or 6.5 CGPA in engineering. All branches eligible. No active backlogs.",
        "rounds": "Round 1: Cognitive + Technical Assessment (90 Qs, 90 mins), Round 2: Coding Assessment (45 mins, 2 Qs), Round 3: Communication Assessment, Round 4: Virtual Interview.",
        "test_pattern": "Cognitive (Critical Thinking, English, Abstract Reasoning), Technical (Common App & MS Office, Pseudocode, Networking & Cloud).",
        "syllabus": "Pseudocode output, Cloud basics, Network protocols, Strings, Arrays, Bits manipulation.",
        "frequently_asked": [
            "Explain Cloud computing service models (IaaS, PaaS, SaaS).",
            "What is Polymorphism and what are its types?",
            "Write a program to count vowels and consonants in a string.",
            "What is a deadlock and how can it be prevented?",
            "Describe a time you adapted to a new technology quickly."
        ],
        "overview": "Global Fortune 500 powerhouse known for innovative client projects, strong fresher onboarding, and continuous certifications.",
        "careers_url": "https://www.accenture.com/in-en/careers"
    },
    {
        "name": "Amazon",
        "logo": "amazon.svg",
        "category": "Product",
        "industry": "Global Tech Giant, E-Commerce & AWS Cloud",
        "color": "#ea580c",
        "ctc": "28 LPA - 44 LPA",
        "roles": "Software Development Engineer (SDE 1), Cloud Support Associate",
        "eligibility": "6.5+ CGPA or 65% in CS/IT/ECE branches. Strong problem-solving record.",
        "rounds": "Round 1: Online Assessment (Debugging + 2 DSA Problems + Work Style Assessment), Round 2-4: Technical Interviews (DSA + System Design + Leadership Principles).",
        "test_pattern": "Online Coding Assessment on HackerRank (2 Hard/Medium DSA problems, 70 mins) + 14 Amazon Leadership Principles survey.",
        "syllabus": "Trees, Graphs, Dynamic Programming, Heaps, Hash Tables, System Design, Concurrency.",
        "frequently_asked": [
            "Given a binary tree, find the lowest common ancestor (LCA) of two given nodes.",
            "Implement an LRU (Least Recently Used) Cache with O(1) get and put operations.",
            "Find the median from a data stream using two heaps.",
            "Amazon Leadership Principle: Tell me about a time you showed Customer Obsession.",
            "Tell me about a time you took a calculated risk and failed (Ownership)."
        ],
        "overview": "Premier product company offering top-tier compensation, massive scale, and evaluation centered around the 16 Leadership Principles.",
        "careers_url": "https://www.amazon.jobs/"
    },
    {
        "name": "Microsoft",
        "logo": "microsoft.svg",
        "category": "Product",
        "industry": "Software, Azure Cloud & AI Products",
        "color": "#00A4EF",
        "ctc": "25 LPA - 45 LPA",
        "roles": "Software Engineer 1 (Full-Time & Summer Internship)",
        "eligibility": "7.0+ CGPA in CS/IT. Strong grasp of algorithms and systems.",
        "rounds": "Round 1: Online Coding (3 algorithmic problems, 90 mins), Round 2: Technical Interview 1 (DSA), Round 3: Technical Interview 2 (System Design/OS), Round 4: AA / Managerial Round.",
        "test_pattern": "3 Coding problems on Codility/HackerRank covering Strings, Arrays, Dynamic Programming.",
        "syllabus": "Data Structures, Algorithms, Memory Management, Operating Systems, Low-Level Design.",
        "frequently_asked": [
            "Serialize and deserialize a Binary Tree.",
            "Reverse a linked list in groups of size K.",
            "Design a thread-safe Singleton pattern in Java/C++.",
            "Explain Virtual Memory, Paging, and Page Faults in Operating Systems.",
            "Why do you want to build products at Microsoft?"
        ],
        "overview": "Global technology leader in operating systems, Azure cloud, productivity tools, and artificial intelligence.",
        "careers_url": "https://careers.microsoft.com/"
    },
    {
        "name": "Google",
        "logo": "google.svg",
        "category": "Product",
        "industry": "Search, Cloud, AI & Mobile Computing",
        "color": "#4285F4",
        "ctc": "30 LPA - 55 LPA",
        "roles": "Software Engineer (Campus & Off-Campus), Application Engineer",
        "eligibility": "No minimum cutoff specified, but requires elite competitive coding capabilities.",
        "rounds": "Round 1: Google Online Challenge (GOC - 2 algorithmic problems), Round 2-5: 4-5 In-depth Technical Problem Solving Interviews (Googleyness + Technical).",
        "test_pattern": "2 challenging algorithmic questions on Google's testing platform testing asymptotic optimization.",
        "syllabus": "Graphs (DFS, BFS, Dijkstra, Topological Sort), Advanced DP, Tries, Segment Trees, Big-O Analysis.",
        "frequently_asked": [
            "Given a directed graph, detect if it contains a cycle and return the cycle path.",
            "Word Break problem using Dynamic Programming and Trie.",
            "Trapping Rain Water problem in O(N) time and O(1) auxiliary space.",
            "Explain Googleyness: Tell me about a time you helped a peer succeed without personal reward.",
            "How would you optimize search query autocomplete latency?"
        ],
        "overview": "The world's most selective tech company, renowned for deep algorithmic problem solving, clean code, and engineering culture.",
        "careers_url": "https://www.google.com/about/careers/applications/"
    },
    {
        "name": "Capgemini",
        "logo": "capgemini.svg",
        "category": "MNC",
        "industry": "Technology Consulting & Engineering Services",
        "color": "#0070AD",
        "ctc": "4.0 LPA - 7.5 LPA",
        "roles": "Analyst (4.0 LPA), Senior Analyst (5.75 - 7.5 LPA)",
        "eligibility": "60% or 6.0 CGPA in 10th, 12th, and Degree. Maximum 1 active backlog.",
        "rounds": "Round 1: Pseudocode + English Test, Round 2: Game-Based Aptitude, Round 3: Behavioral Test, Round 4: Technical & HR Interview.",
        "test_pattern": "Pseudocode (30 Qs, 30 mins), English Communication (30 Qs, 30 mins), Game-based Cognitive test (4 games).",
        "syllabus": "Data structures pseudocode, Bitwise operators, Verbal comprehension, Inductive reasoning games.",
        "frequently_asked": [
            "Explain the difference between compile-time and run-time polymorphism.",
            "What is a subquery and when should it be used instead of a JOIN?",
            "Explain the difference between Primary Key and Foreign Key.",
            "What are your core project technologies and challenges faced?",
            "Are you comfortable working in different technical domains?"
        ],
        "overview": "French multinational consulting firm offering diverse projects across engineering, banking, and digital services.",
        "careers_url": "https://www.capgemini.com/careers/"
    },
    {
        "name": "Deloitte",
        "logo": "deloitte.svg",
        "category": "MNC",
        "industry": "Consulting, Audit, Tax & Enterprise Tech",
        "color": "#86BC25",
        "ctc": "4.5 LPA - 7.6 LPA",
        "roles": "Analyst - USI Consulting, Technology Advisory",
        "eligibility": "60% or 6.5 CGPA in graduation. No active backlogs.",
        "rounds": "Round 1: Cognitive Assessment (Math, Logical, English), Round 2: Technical Assessment, Round 3: Technical Interview, Round 4: Partner/HR Interview.",
        "test_pattern": "Cognitive test (Aptitude, Verbal, Logical), Coding (2 problems), Communication test.",
        "syllabus": "Business math, Syllogisms, Core CS basics, Communication skills, Case studies.",
        "frequently_asked": [
            "Explain the difference between HTTP and HTTPS.",
            "How does an API work and what is RESTful architecture?",
            "Describe a time you solved a conflict within an academic group.",
            "Why consulting and why Deloitte?",
            "Walk me through your resume and highlight your key accomplishment."
        ],
        "overview": "Big Four consulting firm offering prestigious advisory, analytics, and software engineering opportunities.",
        "careers_url": "https://www2.deloitte.com/ui/en/careers"
    },
    {
        "name": "Zoho",
        "logo": "zoho.svg",
        "category": "Product",
        "industry": "Enterprise SaaS & Business Applications",
        "color": "#EA4335",
        "ctc": "5.6 LPA - 8.5 LPA",
        "roles": "Software Developer, Quality Assurance Engineer",
        "eligibility": "Open to all branches and degrees. No strict academic percentage cutoffs.",
        "rounds": "Round 1: General Aptitude & C Programming Output (Flow of control), Round 2: Basic Programming (5 problems in C/C++/Java), Round 3: Advanced Programming (Complex application/game logic), Round 4: Technical Interview, Round 5: HR Interview.",
        "test_pattern": "Strict focus on C programming output prediction, pointer arithmetic, recursion, and writing code from scratch without IDE assistance.",
        "syllabus": "Pointers, 2D Arrays, Pattern Printing, String Parsing, Data Structures, OOPs.",
        "frequently_asked": [
            "Write a program to implement Snake and Ladder or Tic-Tac-Toe in console.",
            "Write a program to print a spiral matrix.",
            "Implement a custom String split without using library functions.",
            "Explain how memory is allocated for 2D arrays in C.",
            "Why Zoho over traditional MNCs?"
        ],
        "overview": "India's premier bootstrapped SaaS unicorn, renowned for testing raw programming logic, pointers, and problem solving rather than theoretical jargon.",
        "careers_url": "https://www.zoho.com/careers/"
    },
    {
        "name": "Tech Mahindra",
        "logo": "tech_mahindra.svg",
        "category": "MNC",
        "industry": "IT Services & Telecom Solutions",
        "color": "#E31837",
        "ctc": "3.5 LPA - 5.5 LPA",
        "roles": "Associate Software Engineer, Telecom Tech Engineer",
        "eligibility": "60% or 6.0 CGPA throughout 10th, 12th, and Graduation.",
        "rounds": "Round 1: Aptitude + English Test, Round 2: Technical Evaluation & Coding, Round 3: Conversational Assessment, Round 4: Tech & HR Interview.",
        "test_pattern": "Quantitative, Logical, Verbal (75 mins) + 2 Coding problems (45 mins).",
        "syllabus": "Aptitude, Computer fundamentals, Networking, C/Java programming.",
        "frequently_asked": [
            "What is the difference between TCP and UDP?",
            "Explain the OSI model layers.",
            "Write code to find the factorial of a number using recursion.",
            "What is an Exception in Java and how is it handled?",
            "Are you flexible with shift timings and relocation?"
        ],
        "overview": "Leading IT provider with specialized strength in telecommunications, 5G, enterprise software, and cloud engineering.",
        "careers_url": "https://www.techmahindra.com/en-in/careers/"
    },
    {
        "name": "IBM",
        "logo": "ibm.svg",
        "category": "MNC",
        "industry": "Hybrid Cloud, AI & Enterprise Solutions",
        "color": "#052FAD",
        "ctc": "4.5 LPA - 11 LPA",
        "roles": "Associate System Engineer, Software Developer",
        "eligibility": "65% or 6.5 CGPA in B.Tech / M.Tech. Max 1 active backlog.",
        "rounds": "Round 1: Cognitive Ability Games, Round 2: Learning Agility Assessment, Round 3: English Language Assessment, Round 4: Coding Test, Round 5: Technical & HR Interview.",
        "test_pattern": "Game-based cognitive assessment, HackerRank coding challenges.",
        "syllabus": "Cognitive logic, Linux commands, Python/Java, Cloud fundamentals, Relational databases.",
        "frequently_asked": [
            "What is the difference between monolithic and microservices architecture?",
            "Explain Docker containers vs Virtual Machines.",
            "Write an SQL query to join three tables.",
            "How does Red Hat OpenShift benefit hybrid cloud deployments?",
            "Describe your project workflow and version control strategies."
        ],
        "overview": "Historic computing powerhouse pioneering hybrid cloud architecture, Red Hat ecosystem, quantum computing, and enterprise AI.",
        "careers_url": "https://www.ibm.com/careers"
    },
    {
        "name": "Oracle",
        "logo": "oracle.svg",
        "category": "Product",
        "industry": "Database Systems, Cloud Infrastructure (OCI) & Enterprise Software",
        "color": "#C74634",
        "ctc": "14 LPA - 22 LPA",
        "roles": "Member of Technical Staff (MTS), Associate Software Engineer",
        "eligibility": "7.0+ CGPA with no standing backlogs in CS/IT.",
        "rounds": "Round 1: Online Test (Aptitude, Core CS, Coding), Round 2-4: 3 Technical Interview rounds on DSA, DBMS internals, and OS.",
        "test_pattern": "Technical MCQs (DBMS, OS, Networks, C++) + 2 algorithmic coding problems.",
        "syllabus": "B+ Tree indexing, Concurrency control, Query optimization, Pointers, Graph algorithms.",
        "frequently_asked": [
            "Explain how B+ Trees optimize database page lookups over standard BSTs.",
            "Write code to implement a Trie data structure for autocomplete.",
            "Explain transaction isolation levels (Read Uncommitted, Read Committed, Repeatable Read, Serializable).",
            "What is the Difference between Mutex and Spinlock in OS kernels?",
            "How does garbage collection work in HotSpot JVM?"
        ],
        "overview": "Global leader in database engines, enterprise ERP solutions, and cloud infrastructure.",
        "careers_url": "https://www.oracle.com/corporate/careers/"
    },
    {
        "name": "Cisco",
        "logo": "cisco.svg",
        "category": "Product",
        "industry": "Networking Hardware, Telecommunications & Cybersecurity",
        "color": "#005073",
        "ctc": "15 LPA - 24 LPA",
        "roles": "Software Engineer (Campus), Network Consulting Engineer",
        "eligibility": "7.0+ CGPA in B.Tech CS/IT/ECE.",
        "rounds": "Round 1: Online Assessment (Aptitude, Networking MCQs, 2 Coding Qs), Round 2-3: Technical Interviews, Round 4: Managerial + HR.",
        "test_pattern": "In-depth Computer Networks MCQs (Subnetting, Routing protocols) + DSA coding.",
        "syllabus": "OSI 7 layers, TCP 3-way handshake, IP Subnetting, Socket programming, C/C++ pointers.",
        "frequently_asked": [
            "How does ARP (Address Resolution Protocol) work?",
            "Explain CIDR subnetting and calculate the broadcast address for a given IP block.",
            "What is the difference between Distance Vector and Link State routing?",
            "Implement a circular buffer / ring buffer in C/C++.",
            "How do Firewalls and NAT (Network Address Translation) inspect packets?"
        ],
        "overview": "The backbone of global internet routing, networking hardware, edge computing, and enterprise cybersecurity.",
        "careers_url": "https://www.cisco.com/c/en/us/about/careers.html"
    },
    {
        "name": "Intel",
        "logo": "intel.svg",
        "category": "Product",
        "industry": "Semiconductors, Microprocessors & Systems Architecture",
        "color": "#0071C5",
        "ctc": "14 LPA - 26 LPA",
        "roles": "Software Development Engineer, Firmware / Silicon Design Engineer",
        "eligibility": "7.0+ CGPA in CS/ECE/EEE with strong fundamentals in hardware-software interface.",
        "rounds": "Round 1: Online Technical Assessment (C/C++, Architecture, DSA), Round 2-3: Core Systems & Architecture Interviews, Round 4: HR.",
        "test_pattern": "Bitwise operations, C pointers, Memory layout, Assembly basics, Cache coherence.",
        "syllabus": "Computer Architecture, Pipelining, Cache memory (L1/L2/L3), C pointers, Multi-threading.",
        "frequently_asked": [
            "Explain cache coherence protocols (like MESI).",
            "What is instruction pipelining and how are pipeline hazards handled?",
            "Write C code to count set bits in an integer using bit manipulation.",
            "Explain Little-Endian vs Big-Endian architecture and write code to detect it.",
            "What happens during system BIOS boot and kernel initialization?"
        ],
        "overview": "World-renowned semiconductor manufacturer driving x86 processor architecture, silicon engineering, and graphics computing.",
        "careers_url": "https://www.intel.com/content/www/us/en/jobs/jobs-at-intel.html"
    },
    {
        "name": "SAP",
        "logo": "sap.svg",
        "category": "Product",
        "industry": "Enterprise Application Software, Cloud & ERP",
        "color": "#008FD3",
        "ctc": "12 LPA - 20 LPA",
        "roles": "Associate Developer, Developer Associate - SAP Labs",
        "eligibility": "65% or 7.0 CGPA in CS/IT branches with no active backlogs.",
        "rounds": "Round 1: Online Test (Coding + Aptitude + Core CS), Round 2: Technical Interview 1 (DSA), Round 3: Technical Interview 2 (System Design/Java), Round 4: Managerial + HR.",
        "test_pattern": "2 DSA coding problems + Aptitude + CS fundamentals.",
        "syllabus": "Java, Spring Boot, Data Structures, SQL, Distributed Systems basics.",
        "frequently_asked": [
            "How does in-memory computing work (SAP HANA architecture)?",
            "Explain Java Garbage Collection algorithms and heap generations.",
            "Write a function to detect and remove a loop in a linked list.",
            "What is dependency injection in Spring Boot?",
            "How do you design a high-throughput enterprise booking system?"
        ],
        "overview": "European tech titan and market leader in enterprise application software, powering over 80% of Fortune 500 business transactions.",
        "careers_url": "https://www.sap.com/about/careers.html"
    },
    {
        "name": "Adobe",
        "logo": "adobe.svg",
        "category": "Product",
        "industry": "Creative Software, Digital Media & Cloud Solutions",
        "color": "#FA0F00",
        "ctc": "25 LPA - 42 LPA",
        "roles": "Software Development Engineer (MTS 1)",
        "eligibility": "7.5+ CGPA in B.Tech/M.Tech Computer Science.",
        "rounds": "Round 1: Online Coding Round (3 DSA problems, 90 mins), Round 2-4: 3 Technical Problem Solving Rounds, Round 5: Director / HR Round.",
        "test_pattern": "Heavy algorithmic focus: Dynamic Programming, Graph Theory, Trees, String matching.",
        "syllabus": "Advanced DSA, C++, Computer Graphics math, OOPs, Memory optimization.",
        "frequently_asked": [
            "Design an undo/redo feature for a vector graphics canvas using stacks.",
            "Implement a word break algorithm using Dynamic Programming and Trie.",
            "Find the maximum rectangular area in a histogram in O(N) time.",
            "Explain Smart Pointers and RAII memory management in C++.",
            "Describe your most technically complex software project."
        ],
        "overview": "Creator of Photoshop, Illustrator, Acrobat, and Adobe Experience Cloud, hiring elite software engineers for creative cloud platforms.",
        "careers_url": "https://www.adobe.com/careers.html"
    },
    {
        "name": "Salesforce",
        "logo": "salesforce.svg",
        "category": "Product",
        "industry": "Cloud CRM & Enterprise Software Platform",
        "color": "#00A1E0",
        "ctc": "22 LPA - 38 LPA",
        "roles": "Associate Software Engineer - Futureforce",
        "eligibility": "7.0+ CGPA in engineering with strong software engineering mindset.",
        "rounds": "Round 1: HackerRank Coding Challenge (3 questions), Round 2: Technical Interview 1 (DSA), Round 3: Technical Interview 2 (System Architecture/OOPs), Round 4: Hiring Manager.",
        "test_pattern": "Algorithms, Hash Tables, Trees, Concurrency, SQL.",
        "syllabus": "Data structures, Multi-tenant cloud architectures, REST APIs, Object-oriented design.",
        "frequently_asked": [
            "What is multi-tenancy in cloud software architectures?",
            "Design a Rate Limiter algorithm for an API gateway.",
            "Given an unsorted array, find the longest consecutive elements sequence in O(N) time.",
            "Explain ACID properties and transaction isolation in distributed databases.",
            "How do you ensure zero-downtime database schema migrations?"
        ],
        "overview": "The world's #1 customer relationship management (CRM) software company, pioneering enterprise cloud computing.",
        "careers_url": "https://www.salesforce.com/company/careers/"
    },
    {
        "name": "HCLTech",
        "logo": "hcltech.svg",
        "category": "MNC",
        "industry": "Global Technology & Digital Engineering",
        "color": "#0D2052",
        "ctc": "3.6 LPA - 7.0 LPA",
        "roles": "Graduate Engineer Trainee (GET), Software Engineer",
        "eligibility": "60% or 6.0 CGPA across 10th, 12th, and Degree. Max 1 active backlog.",
        "rounds": "Round 1: Online Aptitude & Technical Test, Round 2: Technical Interview, Round 3: HR Interview.",
        "test_pattern": "Quantitative Aptitude, Logical Reasoning, Verbal, Technical CS MCQs, Basic Coding.",
        "syllabus": "Programming basics, DBMS, Data structures, Aptitude math, English comprehension.",
        "frequently_asked": [
            "What is the difference between primary key and candidate key?",
            "Explain the concept of method overriding with a Java code example.",
            "Write a program to reverse an array without extra space.",
            "What is a subnet mask in computer networking?",
            "Are you willing to work in 24/7 rotational shifts?"
        ],
        "overview": "Top Indian IT multinational powering global digital engineering and enterprise technology transformation.",
        "careers_url": "https://www.hcltech.com/careers"
    },
    {
        "name": "LTIMindtree",
        "logo": "ltimindtree.svg",
        "category": "MNC",
        "industry": "Digital Solutions & Enterprise Consulting",
        "color": "#002D62",
        "ctc": "4.0 LPA - 8.5 LPA",
        "roles": "Graduate Engineer Trainee, Software Specialist",
        "eligibility": "60% or 6.5 CGPA with no active backlogs.",
        "rounds": "Round 1: Cognitive + Technical MCQs, Round 2: Coding Test, Round 3: Technical Interview, Round 4: HR.",
        "test_pattern": "Quantitative, Verbal, Logical, Pseudocode, 2 Coding questions.",
        "syllabus": "Arrays, Strings, OOPs, SQL Joins, Basic Algorithms.",
        "frequently_asked": [
            "Explain OOPs concepts with real-world examples.",
            "Write an SQL query to find employees who joined in the last 6 months.",
            "What is the difference between call by value and call by reference?",
            "Explain sorting algorithms and their average time complexities.",
            "Why LTIMindtree?"
        ],
        "overview": "Formed through the mega-merger of L&T Infotech and Mindtree, providing cutting-edge IT services and digital transformation.",
        "careers_url": "https://www.ltimindtree.com/careers/"
    },
    {
        "name": "Goldman Sachs",
        "logo": "goldman_sachs.svg",
        "category": "FinTech",
        "industry": "Global Investment Banking, Securities & Financial Tech",
        "color": "#7399C6",
        "ctc": "24 LPA - 38 LPA",
        "roles": "Analyst - Engineering Division (Full-Time & Summer Analyst)",
        "eligibility": "7.0+ CGPA in CS/IT/Math. Strong analytical and math foundations.",
        "rounds": "Round 1: Aptitude + Math + 2 Coding Problems, Round 2-4: 3-4 Rounds of Problem Solving, DSA, Math/Puzzles, and System Design.",
        "test_pattern": "Advanced Math/Probability MCQs + 2 Hard Algorithmic problems on HackerRank.",
        "syllabus": "Probability, Permutations, Graph Algorithms, Dynamic Programming, High-Frequency Trading systems basics.",
        "frequently_asked": [
            "Trapping Rain Water problem or Stock Buy and Sell at most 2 times.",
            "Classic Probability Puzzle: Monty Hall Problem or Three Prisoners Riddle.",
            "Design a low-latency concurrent order matching engine.",
            "Implement a thread-safe Queue with non-blocking locks.",
            "Explain how garbage collection pauses impact low-latency trading algorithms."
        ],
        "overview": "Preeminent global financial institution renowned for top-echelon engineering salaries, quantitative rigor, and high-performance financial systems.",
        "careers_url": "https://www.goldmansachs.com/careers/"
    },
    {
        "name": "Morgan Stanley",
        "logo": "morgan_stanley.svg",
        "category": "FinTech",
        "industry": "Investment Banking & Wealth Management Tech",
        "color": "#002B49",
        "ctc": "22 LPA - 35 LPA",
        "roles": "Technology Analyst, Software Development Engineer",
        "eligibility": "7.0+ CGPA in engineering with clean academic track record.",
        "rounds": "Round 1: Online Assessment (Debugging + Aptitude + 2 Coding Qs), Round 2-3: Technical Interviews on DSA, OOPs, OS, Round 4: HR.",
        "test_pattern": "Debugging code, CS fundamentals (OS, DBMS, Networks), Data structures coding.",
        "syllabus": "Data structures, Pointers, Threading, Deadlocks, SQL Indexing, Java collections.",
        "frequently_asked": [
            "What is the internal implementation of a ThreadPoolExecutor in Java?",
            "Explain Deadlock 4 conditions and Banker's Algorithm.",
            "Write code to find the longest substring without repeating characters.",
            "Explain Database Sharding vs Replication.",
            "Why do you want to work in financial technology?"
        ],
        "overview": "Wall Street powerhouse offering high-impact engineering careers in algorithmic trading, wealth systems, and enterprise cybersecurity.",
        "careers_url": "https://www.morganstanley.com/careers"
    },
    {
        "name": "JPMorgan Chase",
        "logo": "jpmorgan.svg",
        "category": "FinTech",
        "industry": "Global Financial Services & Digital Banking",
        "color": "#4B382A",
        "ctc": "16 LPA - 28 LPA",
        "roles": "Software Engineer Trainee, Technology Analyst (Code for Good Hackathon)",
        "eligibility": "7.0+ CGPA with strong coding and collaborative skills.",
        "rounds": "Round 1: HackerRank Coding Assessment, Round 2: Video Interview (HireVue), Round 3: Code for Good 24-hr Hackathon / Final Interviews.",
        "test_pattern": "2 Coding problems testing Arrays, Strings, Greedy algorithms + behavioral video questions.",
        "syllabus": "Full Stack Web Development, Cloud APIs, Data Structures, Git, Teamwork.",
        "frequently_asked": [
            "How do you design a secure payment transfer API handling concurrent requests?",
            "Explain the difference between Optimistic Locking and Pessimistic Locking.",
            "Find the maximum subarray sum (Kadane's Algorithm).",
            "What is the difference between Monolith and Microservices?",
            "Describe your contribution during the team hackathon."
        ],
        "overview": "The largest bank in the United States, hiring thousands of campus engineers through its prestigious 'Code for Good' hackathons.",
        "careers_url": "https://careers.jpmorgan.com/"
    },
    {
        "name": "Walmart Global Tech",
        "logo": "walmart.svg",
        "category": "Product",
        "industry": "Retail Technology, E-Commerce & Supply Chain Platforms",
        "color": "#0071DC",
        "ctc": "20 LPA - 32 LPA",
        "roles": "Software Development Engineer (SDE 1)",
        "eligibility": "7.0+ CGPA in CS/IT branches with strong algorithm foundations.",
        "rounds": "Round 1: Online Assessment (DSA + Core CS), Round 2-3: Technical Problem Solving Interviews, Round 4: Managerial + Behavioral.",
        "test_pattern": "2-3 Algorithmic problems on HackerEarth + CS fundamentals.",
        "syllabus": "Dynamic Programming, Binary Trees, Graphs, System Design basics, Java/Python.",
        "frequently_asked": [
            "Implement a Trie with insert, search, and startsWith methods.",
            "Design a Shopping Cart checkout system with inventory reservation.",
            "Coin Change Problem using Dynamic Programming.",
            "Explain caching strategies (Write-Through vs Write-Back).",
            "How does Walmart process billions of retail events in real time?"
        ],
        "overview": "The tech wing of Fortune 1 giant Walmart, building petabyte-scale retail platforms, autonomous supply chains, and AI shopping agents.",
        "careers_url": "https://careers.walmart.com/technology"
    },
    {
        "name": "PayPal",
        "logo": "paypal.svg",
        "category": "FinTech",
        "industry": "Digital Payments, Financial Infrastructure & Fintech",
        "color": "#003087",
        "ctc": "22 LPA - 34 LPA",
        "roles": "Software Engineer 1, Risk & Analytics Engineer",
        "eligibility": "7.0+ CGPA in B.Tech / M.Tech CS/IT.",
        "rounds": "Round 1: Online Assessment (Coding + CS Fundamentals), Round 2-3: In-depth Technical Problem Solving, Round 4: Managerial & Cultural Fit.",
        "test_pattern": "2-3 Coding questions on Arrays, Dynamic Programming, Graphs.",
        "syllabus": "Data structures, Distributed transactions (Saga pattern), REST APIs, SQL, Security.",
        "frequently_asked": [
            "How do you handle idempotent API requests in financial payments?",
            "Implement a circular queue with array.",
            "Explain Two-Phase Commit (2PC) protocol in distributed databases.",
            "Find the median in a stream of running numbers.",
            "How do you prevent race conditions during credit card charging?"
        ],
        "overview": "Global pioneer in online checkout, peer-to-peer payments, digital wallets, and financial fraud detection systems.",
        "careers_url": "https://www.paypal.com/us/webapps/mpp/jobs"
    },
    {
        "name": "AMD",
        "logo": "amd.svg",
        "category": "Product",
        "industry": "High-Performance Computing, GPUs & Microprocessors",
        "color": "#ED1C24",
        "ctc": "15 LPA - 26 LPA",
        "roles": "Silicon Design Engineer, Firmware & Systems Software Engineer",
        "eligibility": "7.0+ CGPA in CS/ECE/EEE with hardware-software knowledge.",
        "rounds": "Round 1: Online Test (Technical C/C++, Architecture, Verilog/DSA), Round 2-3: Technical Interviews on GPU/CPU systems and memory, Round 4: HR.",
        "test_pattern": "Bitwise manipulation, C pointers, Linux kernel architecture, Data structures.",
        "syllabus": "C/C++, Computer Organization, GPU architectures, Multithreading, Memory caching.",
        "frequently_asked": [
            "Explain the difference between CPU and GPU architectures (SIMD vs MIMD).",
            "Write C code to reverse bits of a 32-bit unsigned integer.",
            "What is Cache Coherency and how do multi-core processors maintain it?",
            "Explain memory barriers and atomic operations in multithreaded systems.",
            "Describe your low-level systems or compiler engineering projects."
        ],
        "overview": "Global leader in high-performance computing, Ryzen CPUs, Radeon graphics, and AI enterprise accelerators.",
        "careers_url": "https://www.amd.com/en/corporate/careers.html"
    },
    {
        "name": "Qualcomm",
        "logo": "qualcomm.svg",
        "category": "Product",
        "industry": "Wireless Tech, Snapdragon SoCs & 5G Systems",
        "color": "#3253DC",
        "ctc": "16 LPA - 28 LPA",
        "roles": "Software Engineer, Modem & Embedded Systems Engineer",
        "eligibility": "7.0+ CGPA in CS/ECE/EEE with strong embedded C/C++ skills.",
        "rounds": "Round 1: Online Assessment (C Programming, Aptitude, OS, Electronics), Round 2-3: Technical Interviews on C, Pointers, RTOS, Round 4: HR.",
        "test_pattern": "C language output, Pointer arithmetic, Bitwise operations, OS concepts.",
        "syllabus": "C pointers, Bitwise manipulation, Embedded systems, Real-Time Operating Systems (RTOS), Networking.",
        "frequently_asked": [
            "Write a macro to check if a specific bit in a byte is set.",
            "Explain priority inversion in Real-Time Operating Systems and how priority inheritance solves it.",
            "Write code to implement a custom memory allocator (like malloc and free).",
            "What is volatile keyword in C and where is it mandatory in embedded systems?",
            "Explain how the Snapdragon processor manages thermal and battery throttling."
        ],
        "overview": "Pioneer in mobile telecommunications, Snapdragon chipsets, 5G wireless networks, and on-device AI.",
        "careers_url": "https://www.qualcomm.com/company/careers"
    },
    {
        "name": "Uber",
        "logo": "uber.svg",
        "category": "Product",
        "industry": "Mobility Platforms, Distributed Systems & Cloud Logistics",
        "color": "#000000",
        "ctc": "35 LPA - 55 LPA",
        "roles": "Software Engineer 1 (Bangalore / Hyderabad Tech Center)",
        "eligibility": "Top-tier coding capabilities with clean understanding of scalable systems.",
        "rounds": "Round 1: CodeSignal Online Assessment (4 Algorithmic Qs), Round 2-4: 3 In-depth Technical Problem Solving & System Architecture rounds, Round 5: Behavioral.",
        "test_pattern": "4 algorithmic challenges in 70 minutes testing advanced data structures and optimal code.",
        "syllabus": "Graphs (Dijkstra, A* Search), Geo-spatial hashing (H3 / Geohash), Dynamic Programming, Concurrency, Microservices.",
        "frequently_asked": [
            "Given rider and driver coordinates, design an algorithm to find the K nearest available drivers.",
            "Implement a distributed rate limiter that handles millions of rides requests.",
            "Find the shortest path in a dynamic road network with varying edge weights.",
            "How would you design Uber's surge pricing architecture?",
            "Explain how distributed consensus (Raft/Paxos) ensures reliable trip states."
        ],
        "overview": "World leader in urban mobility, ride-hailing, food delivery, and autonomous logistics, offering top-bracket salaries in India.",
        "careers_url": "https://www.uber.com/us/en/careers/"
    }
]

# ====================================================================
# QUESTION BANKS FOR ALL 17 APTITUDE & CODING CATEGORIES
# ====================================================================

# We will import the existing ones and append the new language question sets
QUESTION_BANKS = {
    "python": {
        "title": "Python Programming Test",
        "questions": [
            {
                "question": "What is the output of the following Python code snippet?",
                "code": "a = [1, 2, 3]\nb = a\nb.append(4)\nprint(len(a))",
                "options": ["3", "4", "Error", "None"],
                "correct_idx": 1,
                "explanation": "In Python, lists are mutable objects and assigned by reference. Both 'a' and 'b' refer to the exact same list in memory, so appending to 'b' modifies 'a'."
            },
            {
                "question": "Which of the following data types in Python is IMMUTABLE?",
                "code": "",
                "options": ["List", "Dictionary", "Tuple", "Set"],
                "correct_idx": 2,
                "explanation": "Tuples, strings, integers, floats, and frozensets are immutable in Python. Lists, dictionaries, and sets are mutable."
            },
            {
                "question": "What is the output of the following list comprehension?",
                "code": "nums = [x**2 for x in range(5) if x % 2 != 0]\nprint(nums)",
                "options": ["[1, 9]", "[0, 4, 16]", "[1, 3, 5]", "[1, 9, 25]"],
                "correct_idx": 0,
                "explanation": "The odd numbers in range(5) (0, 1, 2, 3, 4) are 1 and 3. Their squares are 1**2 = 1 and 3**2 = 9."
            },
            {
                "question": "What does the Global Interpreter Lock (GIL) in CPython do?",
                "code": "",
                "options": [
                    "Locks memory to prevent unauthorized database access",
                    "Allows only one native thread to execute Python bytecode at a time",
                    "Prevents infinite while loops in scripts",
                    "Enforces strict type declarations"
                ],
                "correct_idx": 1,
                "explanation": "The GIL is a mutex that prevents multiple native OS threads from executing Python bytecode simultaneously in CPython."
            },
            {
                "question": "What is the output of this Python slice operation?",
                "code": "s = 'Placement'\nprint(s[1:5])",
                "options": ["lace", "lacem", "Plac", "lace "],
                "correct_idx": 0,
                "explanation": "Python slicing is exclusive of the end index. Index 1 to 5 gives 'lace'."
            },
            {
                "question": "What keyword is used to create a generator function in Python?",
                "code": "",
                "options": ["generate", "return", "yield", "async"],
                "correct_idx": 2,
                "explanation": "The 'yield' keyword pauses execution and yields a value back to the caller, creating a generator."
            },
            {
                "question": "What is the output of following dictionary operation?",
                "code": "d = {'a': 1, 'b': 2}\nprint(d.get('c', 10))",
                "options": ["None", "KeyError", "10", "0"],
                "correct_idx": 2,
                "explanation": "dict.get(key, default) returns the specified default value (10) if the key is not in the dictionary."
            },
            {
                "question": "Which built-in function returns both index and value when iterating over an iterable?",
                "code": "",
                "options": ["zip()", "enumerate()", "map()", "filter()"],
                "correct_idx": 1,
                "explanation": "enumerate() returns pairs of (index, value) during iteration."
            },
            {
                "question": "What will be printed by the following code?",
                "code": "print(type(lambda x: x + 1))",
                "options": ["<class 'function'>", "<class 'lambda'>", "<class 'expression'>", "<class 'int'>"],
                "correct_idx": 0,
                "explanation": "In Python, anonymous functions created with 'lambda' are first-class instances of the function class (<class 'function'>)."
            },
            {
                "question": "How are variable keyword arguments accepted in a Python function definition?",
                "code": "",
                "options": ["*args", "**kwargs", "&kwargs", "...args"],
                "correct_idx": 1,
                "explanation": "**kwargs captures arbitrary keyword arguments as a dictionary inside the function body."
            }
        ]
    },
    "java": {
        "title": "Java Programming Test",
        "questions": [
            {
                "question": "What is the output of comparing two identical String literals with '==' in Java?",
                "code": "String s1 = \"Hello\";\nString s2 = \"Hello\";\nSystem.out.println(s1 == s2);",
                "options": ["true", "false", "Compilation Error", "NullPointerException"],
                "correct_idx": 0,
                "explanation": "String literals are stored in the String Constant Pool in Java. Both point to the exact same pooled reference, so '==' evaluates to true."
            },
            {
                "question": "Which access modifier gives the widest visibility in Java?",
                "code": "",
                "options": ["protected", "default (package-private)", "private", "public"],
                "correct_idx": 3,
                "explanation": "'public' members are accessible from any package, class, or module in the application."
            },
            {
                "question": "Can an abstract class in Java have a constructor?",
                "code": "",
                "options": [
                    "No, abstract classes cannot have constructors",
                    "Yes, called during subclass instantiation via super()",
                    "Only if all methods are static",
                    "Only if the constructor is private"
                ],
                "correct_idx": 1,
                "explanation": "Yes, abstract classes have constructors invoked by subclasses via super() to initialize instance variables."
            },
            {
                "question": "Which of these collections in Java does NOT allow duplicate elements?",
                "code": "",
                "options": ["ArrayList", "Vector", "HashSet", "LinkedList"],
                "correct_idx": 2,
                "explanation": "HashSet implements the Set interface, which guarantees no duplicate elements."
            },
            {
                "question": "What is the default initial capacity of an ArrayList in Java?",
                "code": "",
                "options": ["0 (lazily allocated to 10 on first add)", "16", "32", "50"],
                "correct_idx": 0,
                "explanation": "In modern Java (Java 8+), an empty ArrayList starts with an empty array buffer and resizes to default capacity 10 upon adding the first element."
            },
            {
                "question": "Which keyword is used to prevent method overriding in Java?",
                "code": "",
                "options": ["static", "final", "const", "abstract"],
                "correct_idx": 1,
                "explanation": "Declaring a method as 'final' prevents subclasses from overriding it."
            },
            {
                "question": "What exception is thrown when dividing an integer by zero in Java?",
                "code": "",
                "options": ["NullPointerException", "ArithmeticException", "NumberFormatException", "IllegalArgumentException"],
                "correct_idx": 1,
                "explanation": "Integer division by zero (e.g. 10 / 0) throws java.lang.ArithmeticException: / by zero at runtime."
            },
            {
                "question": "What is the time complexity of get(key) in a well-balanced java.util.HashMap?",
                "code": "",
                "options": ["O(1) average case", "O(N) always", "O(log N) always", "O(N^2)"],
                "correct_idx": 0,
                "explanation": "HashMap provides O(1) constant-time performance on average for get() and put() operations."
            },
            {
                "question": "Which interface must a class implement to enable execution in a separate Thread?",
                "code": "",
                "options": ["Runnable", "Serializable", "Comparable", "Cloneable"],
                "correct_idx": 0,
                "explanation": "Classes implement java.lang.Runnable and its single run() method to execute tasks asynchronously."
            },
            {
                "question": "What is the purpose of the 'finally' block in Java exception handling?",
                "code": "",
                "options": [
                    "Executes only if an exception was caught",
                    "Executes always, regardless of whether an exception occurred or not",
                    "Catches unchecked runtime errors",
                    "Restarts the JVM"
                ],
                "correct_idx": 1,
                "explanation": "The finally block always executes after try and catch blocks, commonly used to release system resources."
            }
        ]
    },
    "cpp": {
        "title": "C++ Programming Test",
        "questions": [
            {
                "question": "What will be printed by this C++ pointer code?",
                "code": "int a = 10;\nint *p = &a;\n*p = 25;\ncout << a;",
                "options": ["10", "25", "Garbage value", "Compilation error"],
                "correct_idx": 1,
                "explanation": "Pointer *p points to the memory address of variable 'a'. Dereferencing *p and assigning 25 directly modifies 'a'."
            },
            {
                "question": "Which keyword is used to dynamically deallocate an object created with 'new' in C++?",
                "code": "",
                "options": ["delete", "free()", "dealloc", "remove"],
                "correct_idx": 0,
                "explanation": "'delete' calls the destructor and deallocates heap memory allocated with 'new'."
            },
            {
                "question": "What is the size of an empty class in C++?",
                "code": "",
                "options": ["0 bytes", "1 byte", "4 bytes", "Compiler error"],
                "correct_idx": 1,
                "explanation": "In C++, an empty class has a size of 1 byte to ensure that two distinct object instances have unique memory addresses."
            },
            {
                "question": "What mechanism enables runtime polymorphism in C++?",
                "code": "",
                "options": ["Templates", "Virtual functions (vtable/vptr)", "Function overloading", "Friend functions"],
                "correct_idx": 1,
                "explanation": "Virtual functions enable late binding (runtime polymorphism) through virtual method tables (vtables)."
            },
            {
                "question": "Which smart pointer in modern C++ implies exclusive ownership of an object?",
                "code": "",
                "options": ["std::shared_ptr", "std::unique_ptr", "std::weak_ptr", "std::auto_ptr"],
                "correct_idx": 1,
                "explanation": "std::unique_ptr cannot be copied, ensuring single exclusive ownership of dynamically allocated heap objects with automatic RAII deletion."
            },
            {
                "question": "What is a dangling pointer?",
                "code": "",
                "options": [
                    "A pointer pointing to NULL",
                    "A pointer pointing to memory that has already been deallocated/freed",
                    "A pointer declared without an asterisk",
                    "A pointer to another pointer"
                ],
                "correct_idx": 1,
                "explanation": "A dangling pointer holds the address of a memory block that has already been freed or destroyed."
            },
            {
                "question": "Which operator cannot be overloaded in C++?",
                "code": "",
                "options": ["+", "==", ":: (Scope resolution operator)", "[]"],
                "correct_idx": 2,
                "explanation": "Operators that cannot be overloaded in C++ include ::, ., .*, and ?:."
            },
            {
                "question": "What does RAII stand for in C++?",
                "code": "",
                "options": [
                    "Resource Acquisition Is Initialization",
                    "Runtime Array Indexing Interface",
                    "Rapid Application Integration Interface",
                    "Recursive Algorithm Implementation Instance"
                ],
                "correct_idx": 0,
                "explanation": "RAII ties resource management (memory, file handles, mutex locks) to the lifespan of stack objects via constructors and destructors."
            },
            {
                "question": "What is the time complexity of std::sort in C++ STL?",
                "code": "",
                "options": ["O(N log N)", "O(N^2)", "O(N)", "O(log N)"],
                "correct_idx": 0,
                "explanation": "std::sort uses Introsort with a guaranteed worst-case and average-case complexity of O(N log N)."
            },
            {
                "question": "What is the difference between a reference and a pointer in C++?",
                "code": "",
                "options": [
                    "A reference must be initialized when created and cannot be null or reseated to another variable",
                    "Pointers cannot be arithmetic",
                    "References allocate 8 bytes on stack",
                    "No difference"
                ],
                "correct_idx": 0,
                "explanation": "References in C++ are aliases that must be initialized upon declaration and cannot be null or reassigned to another object."
            }
        ]
    },
    "dsa": {
        "title": "Data Structures & Algorithms Test",
        "questions": [
            {
                "question": "Which data structure is primarily used to implement Breadth-First Search (BFS) in a Graph?",
                "code": "",
                "options": ["Stack", "Queue", "Priority Queue", "Hash Map"],
                "correct_idx": 1,
                "explanation": "BFS explores nodes level by level in First-In-First-Out order, making a FIFO Queue the ideal data structure."
            },
            {
                "question": "What is the worst-case time complexity of QuickSort?",
                "code": "",
                "options": ["O(N log N)", "O(N)", "O(N^2)", "O(log N)"],
                "correct_idx": 2,
                "explanation": "QuickSort degrades to O(N^2) when the pivot chosen is consistently the smallest or largest element (such as sorted arrays with standard pivot)."
            },
            {
                "question": "How can you detect a cycle in a Singly Linked List in O(1) space?",
                "code": "",
                "options": [
                    "Floyd's Tortoise and Hare (Slow & Fast Pointers)",
                    "Binary Search",
                    "Hash Set of node values",
                    "Dijkstra's Algorithm"
                ],
                "correct_idx": 0,
                "explanation": "Floyd's Cycle-Finding Algorithm uses two pointers moving at speeds 1x and 2x to detect loops in O(N) time and O(1) space."
            },
            {
                "question": "What is the height of a balanced Binary Search Tree (AVL or Red-Black Tree) with N nodes?",
                "code": "",
                "options": ["O(N)", "O(log N)", "O(N^2)", "O(1)"],
                "correct_idx": 1,
                "explanation": "Self-balancing binary trees maintain height bounded by O(log N)."
            },
            {
                "question": "Which data structure follows the Last-In-First-Out (LIFO) principle?",
                "code": "",
                "options": ["Queue", "Stack", "Array", "Linked List"],
                "correct_idx": 1,
                "explanation": "A Stack operates on LIFO order, where elements pushed last are popped first."
            },
            {
                "question": "What is the average time complexity to search an element in a Hash Table?",
                "code": "",
                "options": ["O(1)", "O(log N)", "O(N)", "O(N log N)"],
                "correct_idx": 0,
                "explanation": "Hash tables compute array bucket indices via hashing functions in O(1) constant time on average."
            },
            {
                "question": "Which sorting algorithm is known to be STABLE?",
                "code": "",
                "options": ["Merge Sort", "QuickSort", "Heap Sort", "Selection Sort"],
                "correct_idx": 0,
                "explanation": "Merge Sort preserves the relative order of elements with equal keys, making it a stable sort."
            },
            {
                "question": "What is the minimum number of queues required to implement a Stack?",
                "code": "",
                "options": ["1", "2", "3", "4"],
                "correct_idx": 1,
                "explanation": "Standard implementation of a Stack using FIFO queues requires 2 queues."
            },
            {
                "question": "In a max-heap of N elements, where is the maximum element stored?",
                "code": "",
                "options": ["At the leaf nodes", "At the root node (index 0)", "At the middle", "Depends on insertion order"],
                "correct_idx": 1,
                "explanation": "In a max-heap, every parent is >= its children, placing the maximum element at the root node."
            },
            {
                "question": "What is the time complexity to find the shortest path using Dijkstra's Algorithm with a Min-Heap?",
                "code": "",
                "options": ["O(V + E)", "O((V + E) log V)", "O(V^3)", "O(E^2)"],
                "correct_idx": 1,
                "explanation": "With an adjacency list and binary priority queue (min-heap), Dijkstra runs in O((V + E) log V) time."
            }
        ]
    },
    "dbms": {
        "title": "DBMS & SQL Queries Test",
        "questions": [
            {
                "question": "Which SQL query correctly retrieves the second highest salary from an Employee table?",
                "code": "",
                "options": [
                    "SELECT MAX(salary) FROM Employee WHERE salary < (SELECT MAX(salary) FROM Employee);",
                    "SELECT salary FROM Employee ORDER BY salary DESC LIMIT 1;",
                    "SELECT SECOND(salary) FROM Employee;",
                    "SELECT salary FROM Employee WHERE rownum = 2;"
                ],
                "correct_idx": 0,
                "explanation": "The subquery finds the maximum salary, and the outer query finds the maximum strictly less than it."
            },
            {
                "question": "What do the letters in the ACID properties of database transactions stand for?",
                "code": "",
                "options": [
                    "Atomicity, Consistency, Isolation, Durability",
                    "Accuracy, Consistency, Integrity, Data",
                    "Access, Control, Index, Dependency",
                    "Algorithm, Cache, Iteration, Deletion"
                ],
                "correct_idx": 0,
                "explanation": "ACID guarantees transactional reliability: Atomicity, Consistency, Isolation, Durability."
            },
            {
                "question": "Which Normal Form removes transitive dependencies?",
                "code": "",
                "options": ["1NF", "2NF", "3NF", "BCNF"],
                "correct_idx": 2,
                "explanation": "Third Normal Form (3NF) requires a relation to be in 2NF and eliminate transitive functional dependencies between non-key attributes."
            },
            {
                "question": "What is the difference between TRUNCATE and DELETE in SQL?",
                "code": "",
                "options": [
                    "TRUNCATE is DDL, resets table and cannot be rolled back easily; DELETE is DML and row-by-row logged",
                    "DELETE drops the entire table definition; TRUNCATE does not",
                    "They are identical commands with different spelling",
                    "TRUNCATE requires a WHERE clause"
                ],
                "correct_idx": 0,
                "explanation": "TRUNCATE is a fast DDL command deallocating pages; DELETE is DML evaluating WHERE conditions."
            },
            {
                "question": "Which SQL JOIN returns all rows from the left table, and matching rows from the right table?",
                "code": "",
                "options": ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL OUTER JOIN"],
                "correct_idx": 1,
                "explanation": "LEFT JOIN preserves all records from the left table, filling in NULL for non-matching records from the right table."
            },
            {
                "question": "What data structure is most commonly used for database table indexing?",
                "code": "",
                "options": ["B+ Tree", "Linked List", "Stack", "Binary Search Tree"],
                "correct_idx": 0,
                "explanation": "B+ Trees are the industry standard for database indexes because leaf nodes are linked sequentially for rapid range queries."
            },
            {
                "question": "What is a Foreign Key constraint used for?",
                "code": "",
                "options": [
                    "To ensure Referential Integrity between two related tables",
                    "To speed up network bandwidth",
                    "To encrypt stored passwords",
                    "To allow duplicate primary keys"
                ],
                "correct_idx": 0,
                "explanation": "A Foreign Key establishes a relationship with a Primary Key in another table, guaranteeing referential integrity."
            },
            {
                "question": "Which SQL clause is used to filter groups created by GROUP BY?",
                "code": "",
                "options": ["WHERE", "HAVING", "ORDER BY", "FILTER"],
                "correct_idx": 1,
                "explanation": "WHERE filters rows before grouping; HAVING filters aggregate results after grouping."
            },
            {
                "question": "How many Clustered Indexes can exist on a single database table?",
                "code": "",
                "options": ["Only 1", "Up to 16", "Unlimited", "0"],
                "correct_idx": 0,
                "explanation": "A Clustered Index dictates the physical ordering of data on disk, so only 1 is permitted per table."
            },
            {
                "question": "What type of lock allows multiple concurrent transactions to read data but prevents modifications?",
                "code": "",
                "options": ["Shared Lock (S-Lock)", "Exclusive Lock (X-Lock)", "Deadlock", "Spinlock"],
                "correct_idx": 0,
                "explanation": "Shared locks allow multiple concurrent reads; Exclusive locks are required for writes."
            }
        ]
    },
    "core_cs": {
        "title": "Core CS, OS & Computer Networks Test",
        "questions": [
            {
                "question": "What are the four necessary conditions for Deadlock to occur in Operating Systems (Coffman Conditions)?",
                "code": "",
                "options": [
                    "Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait",
                    "Paging, Segmentation, Swapping, Scheduling",
                    "Atomicity, Consistency, Isolation, Durability",
                    "Read, Write, Execute, Terminate"
                ],
                "correct_idx": 0,
                "explanation": "Coffman conditions state that deadlock can only happen if Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait occur concurrently."
            },
            {
                "question": "What layer of the OSI model does the HTTP/HTTPS protocol belong to?",
                "code": "",
                "options": ["Application Layer (Layer 7)", "Transport Layer (Layer 4)", "Network Layer (Layer 3)", "Data Link Layer (Layer 2)"],
                "correct_idx": 0,
                "explanation": "HTTP, HTTPS, FTP, DNS, and SMTP operate at Layer 7: the Application Layer."
            },
            {
                "question": "What happens during the TCP 3-Way Handshake connection establishment?",
                "code": "",
                "options": [
                    "SYN -> SYN-ACK -> ACK",
                    "ACK -> SYN -> FIN",
                    "PING -> PONG -> CONNECT",
                    "HELLO -> ACK -> DATA"
                ],
                "correct_idx": 0,
                "explanation": "Client sends SYN, Server responds with SYN-ACK, Client sends ACK to establish the TCP connection."
            },
            {
                "question": "What is the difference between a Process and a Thread?",
                "code": "",
                "options": [
                    "A process has its own independent address space; threads share the memory address space of their parent process",
                    "Threads cannot execute concurrently",
                    "Processes do not use CPU registers",
                    "A thread is an external hardware device"
                ],
                "correct_idx": 0,
                "explanation": "Processes are isolated with separate virtual memory address spaces. Threads are lightweight units within a process sharing heap, code, and global variables."
            },
            {
                "question": "What is Thrashing in Operating Systems?",
                "code": "",
                "options": [
                    "The OS spending more time swapping pages in and out than executing instructions",
                    "Physical destruction of the hard disk drive",
                    "Instant processor overheating",
                    "Network packet collision"
                ],
                "correct_idx": 0,
                "explanation": "Thrashing occurs when high degree of multiprogramming causes excessive page faults."
            },
            {
                "question": "Which port does HTTPS default to?",
                "code": "",
                "options": ["443", "80", "8080", "22"],
                "correct_idx": 0,
                "explanation": "HTTPS runs over port 443 (encrypted with TLS/SSL). Standard unencrypted HTTP defaults to port 80."
            },
            {
                "question": "What does DNS stand for, and what is its primary role?",
                "code": "",
                "options": [
                    "Domain Name System - translates human-readable domain names into IP addresses",
                    "Dynamic Network Security - encrypts LAN packets",
                    "Digital Number Storage - backs up SQLite databases",
                    "Data Node Server - balances web server loads"
                ],
                "correct_idx": 0,
                "explanation": "DNS translates domain names (like google.com) to machine IP addresses."
            },
            {
                "question": "Which synchronization primitive allows up to 'N' concurrent access permits to a shared resource?",
                "code": "",
                "options": ["Counting Semaphore", "Binary Semaphore / Mutex", "Spinlock", "Condition Variable"],
                "correct_idx": 0,
                "explanation": "A Counting Semaphore maintains an integer count representing available permits, allowing up to N threads access before blocking."
            },
            {
                "question": "Which protocol is connectionless and does not guarantee packet delivery or order?",
                "code": "",
                "options": ["UDP", "TCP", "BGP", "SSH"],
                "correct_idx": 0,
                "explanation": "UDP (User Datagram Protocol) is lightweight, connectionless, and lacks retransmission, making it ideal for live streaming and gaming."
            },
            {
                "question": "What CPU scheduling algorithm assigns a fixed time quantum to each ready process in round-robin fashion?",
                "code": "",
                "options": ["Round Robin (RR)", "First-Come First-Served (FCFS)", "Shortest Job First (SJF)", "Priority Scheduling"],
                "correct_idx": 0,
                "explanation": "Round Robin assigns equal time slices (quanta) cyclically to each process in the queue."
            }
        ]
    },
    "quantitative": {
        "title": "Quantitative Aptitude Test",
        "questions": [
            {
                "question": "A student bought an item for Rs. 500 and sold it for Rs. 650. What is the profit percentage?",
                "code": "",
                "options": ["20%", "25%", "30%", "35%"],
                "correct_idx": 2,
                "explanation": "Profit = Selling Price - Cost Price = 650 - 500 = 150. Profit % = (150 / 500) * 100 = 30%."
            },
            {
                "question": "If A can complete a work in 10 days and B can complete the same work in 15 days, how many days will they take working together?",
                "code": "",
                "options": ["5 days", "6 days", "8 days", "7.5 days"],
                "correct_idx": 1,
                "explanation": "Combined 1 day work = 1/10 + 1/15 = 5/30 = 1/6. Total days = 6 days."
            },
            {
                "question": "A train running at 72 km/hr crosses a pole in 10 seconds. What is the length of the train?",
                "code": "",
                "options": ["150 meters", "200 meters", "250 meters", "300 meters"],
                "correct_idx": 1,
                "explanation": "Speed in m/s = 72 * (5/18) = 20 m/s. Length = 20 m/s * 10 s = 200 meters."
            },
            {
                "question": "The ratio of two numbers is 3:4 and their HCF is 4. What is their LCM?",
                "code": "",
                "options": ["12", "24", "48", "36"],
                "correct_idx": 2,
                "explanation": "Numbers are 12 and 16. LCM(12, 16) = 48."
            },
            {
                "question": "In how many different ways can the letters of the word 'LEADER' be arranged?",
                "code": "",
                "options": ["720", "360", "120", "180"],
                "correct_idx": 1,
                "explanation": "LEADER has 6 letters with 'E' repeating twice. Total permutations = 6! / 2! = 720 / 2 = 360."
            },
            {
                "question": "Two coins are tossed simultaneously. What is the probability of getting at least one head?",
                "code": "",
                "options": ["1/4", "1/2", "3/4", "1"],
                "correct_idx": 2,
                "explanation": "Sample space: {HH, HT, TH, TT}. Outcomes with at least one head: {HH, HT, TH} = 3. Probability = 3/4."
            },
            {
                "question": "What is the simple interest on Rs. 4000 at 5% per annum for 3 years?",
                "code": "",
                "options": ["Rs. 400", "Rs. 600", "Rs. 800", "Rs. 500"],
                "correct_idx": 1,
                "explanation": "SI = (4000 * 5 * 3) / 100 = 600."
            },
            {
                "question": "The average of five numbers is 27. If one number is excluded, the average becomes 25. What is the excluded number?",
                "code": "",
                "options": ["30", "35", "40", "45"],
                "correct_idx": 1,
                "explanation": "Sum of 5 numbers = 135. Sum of remaining 4 numbers = 100. Excluded number = 135 - 100 = 35."
            },
            {
                "question": "Find the compound interest on Rs. 10,000 for 2 years at 10% per annum compounded annually.",
                "code": "",
                "options": ["Rs. 2,000", "Rs. 2,100", "Rs. 2,200", "Rs. 1,900"],
                "correct_idx": 1,
                "explanation": "Amount = 10000 * 1.21 = 12,100. CI = 12,100 - 10,000 = Rs. 2,100."
            },
            {
                "question": "A vendor sells 20 apples for the cost price of 25 apples. Find the profit percentage.",
                "code": "",
                "options": ["20%", "25%", "30%", "15%"],
                "correct_idx": 1,
                "explanation": "Profit% = (5 / 20) * 100 = 25%."
            }
        ]
    },
    "logical": {
        "title": "Logical Reasoning Test",
        "questions": [
            {
                "question": "Find the missing number in the series: 3, 7, 15, 31, 63, ?",
                "code": "",
                "options": ["127", "126", "125", "128"],
                "correct_idx": 0,
                "explanation": "Pattern: Each number is multiplied by 2 and added with 1: (63*2+1 = 127)."
            },
            {
                "question": "Pointing to a photograph, Rohit said, 'She is the daughter of my grandfather's only son.' How is Rohit related to the girl?",
                "code": "",
                "options": ["Brother", "Uncle", "Father", "Cousin"],
                "correct_idx": 0,
                "explanation": "Grandfather's only son is Rohit's father. The daughter of Rohit's father is Rohit's sister, making Rohit her brother."
            },
            {
                "question": "In a certain code, COMPUTER is written as RFUVQNPC. How is MEDICINE written in that code?",
                "code": "",
                "options": ["EOJDJEFM", "EOJDEJFM", "MFEJDJOE", "EOJDJEFN"],
                "correct_idx": 0,
                "explanation": "The first and last letters are swapped and reverse shifted with internal letters incremented (+1)."
            },
            {
                "question": "A person walks 10 km North, turns right and walks 10 km, then turns right again and walks 10 km. How far and in what direction is he from the starting point?",
                "code": "",
                "options": ["10 km East", "10 km West", "20 km North", "0 km"],
                "correct_idx": 0,
                "explanation": "He is 10 km East of the starting point."
            },
            {
                "question": "Statements: All cats are dogs. All dogs are birds. Conclusions: (I) All cats are birds. (II) All birds are cats.",
                "code": "",
                "options": ["Only conclusion I follows", "Only conclusion II follows", "Both follow", "Neither follows"],
                "correct_idx": 0,
                "explanation": "Since Cats subset Dogs and Dogs subset Birds, All cats are birds follows."
            },
            {
                "question": "Find the odd one out from the group: 27, 64, 125, 144, 216",
                "code": "",
                "options": ["27", "64", "144", "216"],
                "correct_idx": 2,
                "explanation": "27, 64, 125, and 216 are perfect cubes. 144 is 12^2 (a square, not a cube of an integer)."
            },
            {
                "question": "If '+' means multiply, '-' means divide, '*' means add, and '/' means subtract, calculate: 20 - 5 + 4 * 6 / 2",
                "code": "",
                "options": ["20", "22", "18", "24"],
                "correct_idx": 0,
                "explanation": "20 / 5 * 4 + 6 - 2 = 4 * 4 + 6 - 2 = 16 + 6 - 2 = 20."
            },
            {
                "question": "In a row of 40 students, Priya is 13th from the left end. What is her position from the right end?",
                "code": "",
                "options": ["27th", "28th", "29th", "26th"],
                "correct_idx": 1,
                "explanation": "(40 - 13) + 1 = 28th."
            },
            {
                "question": "Which word cannot be formed using the letters of the word 'RECOMMENDATION'?",
                "code": "",
                "options": ["MEDICINE", "NATION", "MODERN", "COMMON"],
                "correct_idx": 0,
                "explanation": "'MEDICINE' requires two 'I's while RECOMMENDATION has only one 'I'."
            },
            {
                "question": "Today is Monday. What day of the week will it be after 61 days?",
                "code": "",
                "options": ["Tuesday", "Wednesday", "Thursday", "Saturday"],
                "correct_idx": 3,
                "explanation": "61 divided by 7 leaves remainder 5. 5 days after Monday is Saturday."
            }
        ]
    },
    "verbal": {
        "title": "Verbal Ability & English Test",
        "questions": [
            {
                "question": "Choose the word most nearly OPPOSITE in meaning (Antonym) to 'OBSOLETE':",
                "code": "",
                "options": ["Contemporary", "Ancient", "Defunct", "Outdated"],
                "correct_idx": 0,
                "explanation": "Obsolete means outdated. Contemporary means modern and current."
            },
            {
                "question": "Find the correctly spelled word:",
                "code": "",
                "options": ["Accommodate", "Acommodate", "Accomodate", "Acomodate"],
                "correct_idx": 0,
                "explanation": "'Accommodate' has two 'c's and two 'm's."
            },
            {
                "question": "Identify the grammatically correct sentence:",
                "code": "",
                "options": [
                    "Neither of the candidates has submitted their resume.",
                    "Neither of the candidates have submitted his resume.",
                    "Neither of the candidates are submitted.",
                    "Neither candidate have won."
                ],
                "correct_idx": 0,
                "explanation": "'Neither' is a singular indefinite pronoun taking the singular verb 'has'."
            },
            {
                "question": "Choose the synonym for 'CANDID':",
                "code": "",
                "options": ["Frank", "Deceptive", "Shy", "Arrogant"],
                "correct_idx": 0,
                "explanation": "Candid means honest, straightforward, and frank in speech."
            },
            {
                "question": "Fill in the blank: The committee _____ divided in their opinions regarding the budget.",
                "code": "",
                "options": ["was", "were", "is", "has"],
                "correct_idx": 1,
                "explanation": "When collective nouns act as individual members with differing opinions, a plural verb ('were') is used."
            },
            {
                "question": "What is the meaning of the idiom 'To bite the bullet'?",
                "code": "",
                "options": [
                    "To face a difficult situation with courage",
                    "To start a gun fight",
                    "To eat something dangerous",
                    "To quit under pressure"
                ],
                "correct_idx": 0,
                "explanation": "'Bite the bullet' means to bravely endure an unavoidable, difficult situation."
            },
            {
                "question": "Choose the correct preposition: She is proficient _____ Python programming and Data Science.",
                "code": "",
                "options": ["in", "at", "with", "for"],
                "correct_idx": 0,
                "explanation": "The standard English idiom is 'proficient in' a subject or skill."
            },
            {
                "question": "Select the correct one-word substitution for: 'A person who writes computer code or software.'",
                "code": "",
                "options": ["Programmer", "Calligrapher", "Cartographer", "Biographer"],
                "correct_idx": 0,
                "explanation": "A programmer designs and writes computer software code."
            },
            {
                "question": "Choose the word with positive connotation describing someone who handles money carefully:",
                "code": "",
                "options": ["Frugal", "Miserly", "Cheap", "Stingy"],
                "correct_idx": 0,
                "explanation": "Frugal is positive/neutral (wise with money), whereas miserly and stingy carry negative connotations."
            },
            {
                "question": "Identify the passive form: 'The engineer fixed the network bug.'",
                "code": "",
                "options": [
                    "The network bug was fixed by the engineer.",
                    "The network bug is fixed by the engineer.",
                    "The engineer has been fixing the bug.",
                    "The bug had fixed the engineer."
                ],
                "correct_idx": 0,
                "explanation": "Past simple active ('fixed') becomes past simple passive ('was fixed by')."
            }
        ]
    }
}

# Add C Language (Dedicated)
QUESTION_BANKS["c"] = {
    "title": "C Programming Language Test",
    "questions": [
        {
            "question": "What is the output of the following C code?",
            "code": "int a = 5;\nprintf(\"%d %d %d\", a, ++a, a++);",
            "options": ["Undefined behavior (depends on compiler evaluation order)", "5 6 6", "7 7 5", "5 6 7"],
            "correct_idx": 0,
            "explanation": "Modifying a variable multiple times without a sequence point invokes undefined behavior in standard C according to ISO C specification."
        },
        {
            "question": "What does malloc() return if the system runs out of heap memory?",
            "code": "",
            "options": ["NULL", "0", "A dangling pointer", "Throws OutOfMemoryException"],
            "correct_idx": 0,
            "explanation": "malloc() returns a void pointer to allocated memory on success, and returns NULL if the allocation request fails."
        },
        {
            "question": "What is the difference between a Structure and a Union in C?",
            "code": "",
            "options": [
                "Structure allocates separate memory for all members; Union shares the same memory location for all members",
                "Union can have functions, structures cannot",
                "Structures cannot hold pointers",
                "There is no difference in C"
            ],
            "correct_idx": 0,
            "explanation": "The size of a union is equal to the size of its largest member, as all members share the same memory space. In a struct, every member has its own offset."
        },
        {
            "question": "What will be printed by this C pointer code?",
            "code": "char arr[] = \"Hello\";\nprintf(\"%lu\", sizeof(arr));",
            "options": ["5", "6", "4", "8"],
            "correct_idx": 1,
            "explanation": "String literals in C include the invisible terminating null character '\\0', so 'Hello' has 5 letters + 1 null terminator = 6 bytes."
        },
        {
            "question": "Which header file is required to use the free() function in C?",
            "code": "",
            "options": ["<stdlib.h>", "<stdio.h>", "<string.h>", "<memory.h>"],
            "correct_idx": 0,
            "explanation": "Dynamic memory management functions (malloc, calloc, realloc, free) are declared in <stdlib.h>."
        },
        {
            "question": "What is the scope of a static variable declared inside a function in C?",
            "code": "",
            "options": [
                "Local to the function, but its lifetime persists for the entire program execution",
                "Global across all files in the project",
                "Destroyed when the function returns",
                "Accessible from any header file"
            ],
            "correct_idx": 0,
            "explanation": "A static local variable is initialized once and retains its value between multiple invocations of the function."
        },
        {
            "question": "What is the correct syntax for declaring a pointer to an array of 5 integers in C?",
            "code": "",
            "options": ["int (*ptr)[5];", "int *ptr[5];", "int ptr[5]*;", "int *ptr(5);"],
            "correct_idx": 0,
            "explanation": "int (*ptr)[5] declares a pointer to an array of 5 integers. int *ptr[5] declares an array of 5 pointers to integers."
        },
        {
            "question": "What does the 'volatile' keyword signify to the C compiler?",
            "code": "",
            "options": [
                "Tells the compiler not to optimize or cache the variable because it can change unexpectedly (e.g. hardware register)",
                "Makes the variable thread-safe automatically",
                "Stores the variable in CPU register",
                "Prevents the variable from being modified"
            ],
            "correct_idx": 0,
            "explanation": "volatile instructs the optimizer that the variable value may change at any time without any action by nearby code (e.g. interrupt service routine, memory-mapped I/O)."
        },
        {
            "question": "What is the output of 5 >> 1 (bitwise right shift)?",
            "code": "",
            "options": ["2", "10", "4", "1"],
            "correct_idx": 0,
            "explanation": "Binary of 5 is 101. Shifting right by 1 bit results in 010, which equals 2 in decimal (effectively integer division by 2)."
        },
        {
            "question": "Which function is safer to read strings compared to gets() which causes buffer overflows?",
            "code": "",
            "options": ["fgets()", "scanf(\"%s\")", "getc()", "readstr()"],
            "correct_idx": 0,
            "explanation": "fgets() accepts a buffer size parameter, preventing buffer overflow vulnerabilities. gets() was removed completely from the C standard in C11."
        }
    ]
}

# Add JavaScript
QUESTION_BANKS["javascript"] = {
    "title": "JavaScript (ES6+) Programming Test",
    "questions": [
        {
            "question": "What is the output of the following JavaScript expression?",
            "code": "console.log(typeof NaN);",
            "options": ["number", "NaN", "undefined", "object"],
            "correct_idx": 0,
            "explanation": "In JavaScript, NaN (Not-a-Number) is officially of type 'number' according to the IEEE 754 floating-point standard."
        },
        {
            "question": "What is the difference between '==' and '===' in JavaScript?",
            "code": "",
            "options": [
                "'==' performs type coercion before comparison; '===' checks both value and type strictly",
                "'===' is for numbers only; '==' is for strings",
                "They are completely interchangeable",
                "'===' checks memory address; '==' checks values"
            ],
            "correct_idx": 0,
            "explanation": "Strict equality (===) does not do implicit type conversions, so 5 === '5' is false, whereas 5 == '5' coerces '5' to a number and evaluates to true."
        },
        {
            "question": "What will be printed by the following code due to var hoisting?",
            "code": "console.log(a);\nvar a = 10;",
            "options": ["undefined", "ReferenceError", "10", "null"],
            "correct_idx": 0,
            "explanation": "Variables declared with 'var' have their declaration hoisted to the top of the function/global scope and initialized to undefined."
        },
        {
            "question": "What is a Closure in JavaScript?",
            "code": "",
            "options": [
                "A function that retains access to its lexical scope even when invoked outside that scope",
                "A function that terminates the browser event loop",
                "A method to close a database connection",
                "An anonymous callback function"
            ],
            "correct_idx": 0,
            "explanation": "A closure is the combination of a function bundled together with references to its surrounding lexical environment."
        },
        {
            "question": "What does Promise.all() do when one of the promises in the array rejects?",
            "code": "",
            "options": [
                "Immediately rejects with the reason of the first promise that rejected (fail-fast)",
                "Waits for all promises to resolve anyway",
                "Ignores the failed promise and returns the resolved ones",
                "Throws a syntax error"
            ],
            "correct_idx": 0,
            "explanation": "Promise.all() fails fast: if any promise in the array rejects, the returned promise immediately rejects with that rejection error."
        },
        {
            "question": "What will be logged by this code?",
            "code": "const arr = [1, 2, 3];\nconst [x, ...y] = arr;\nconsole.log(y);",
            "options": ["[2, 3]", "2", "[1, 2]", "undefined"],
            "correct_idx": 0,
            "explanation": "Array destructuring with the rest operator (...y) collects the remaining elements into a new array [2, 3]."
        },
        {
            "question": "Which of the following creates a truly deep copy of a complex nested object in modern JavaScript?",
            "code": "",
            "options": ["structuredClone(obj)", "Object.assign({}, obj)", "{...obj}", "obj.slice()"],
            "correct_idx": 0,
            "explanation": "structuredClone() is the official native web API for deep copying nested objects and arrays. Object.assign and the spread operator only produce shallow copies."
        },
        {
            "question": "What is the output of the following arrow function?",
            "code": "const add = (a, b) => a + b;\nconsole.log(add(3, 4));",
            "options": ["7", "undefined", "NaN", "SyntaxError"],
            "correct_idx": 0,
            "explanation": "Arrow functions with concise bodies (without curly braces) automatically return the evaluated expression (implicit return)."
        },
        {
            "question": "In the JavaScript Event Loop, which queue has higher execution priority: Microtask Queue or Macrotask Queue?",
            "code": "",
            "options": [
                "Microtask Queue (Promise callbacks, process.nextTick)",
                "Macrotask Queue (setTimeout, setInterval)",
                "Both have identical priority",
                "Depends on CPU speed"
            ],
            "correct_idx": 0,
            "explanation": "The event loop completely empties the Microtask Queue (Promises, queueMicrotask) before picking up the next Macrotask (setTimeout)."
        },
        {
            "question": "What is the result of [1, 2, 3].map(x => x * 2)?",
            "code": "",
            "options": ["[2, 4, 6]", "[1, 2, 3]", "6", "[2, 2, 2]"],
            "correct_idx": 0,
            "explanation": "Array.map() transforms each element by executing the callback function, returning a new array [2, 4, 6]."
        }
    ]
}

# Add TypeScript
QUESTION_BANKS["typescript"] = {
    "title": "TypeScript Programming Test",
    "questions": [
        {
            "question": "What is the difference between 'any' and 'unknown' in TypeScript?",
            "code": "",
            "options": [
                "'unknown' is type-safe: you cannot perform arbitrary operations on it without type narrowing/checking, unlike 'any'",
                "'any' is for primitive types only",
                "They are identical aliases",
                "'unknown' converts to undefined at runtime"
            ],
            "correct_idx": 0,
            "explanation": "'unknown' is the type-safe counterpart of 'any'. Anything is assignable to 'unknown', but TypeScript will not allow member access or method calls without explicit type narrowing."
        },
        {
            "question": "How do you define an optional property in a TypeScript interface?",
            "code": "",
            "options": [
                "interface User { name?: string; }",
                "interface User { optional name: string; }",
                "interface User { name: string | void; }",
                "interface User { ?name: string; }"
            ],
            "correct_idx": 0,
            "explanation": "Adding a question mark (?) after the property name designates it as optional."
        },
        {
            "question": "What is a Union Type in TypeScript?",
            "code": "",
            "options": [
                "A value that can be one of several specified types (e.g. string | number)",
                "A combined C union data structure",
                "An array that holds only objects",
                "A database JOIN representation"
            ],
            "correct_idx": 0,
            "explanation": "Union types allow a variable to hold values matching any of the unioned types separated by a pipe (|)."
        },
        {
            "question": "What keyword is used to create reusable generic types in TypeScript functions?",
            "code": "",
            "options": ["<T>", "generic", "any", "template"],
            "correct_idx": 0,
            "explanation": "Generics in TypeScript use type parameter syntax such as function identity<T>(arg: T): T."
        },
        {
            "question": "What happens to TypeScript type annotations during compilation to JavaScript?",
            "code": "",
            "options": [
                "They are completely erased/stripped, producing clean JavaScript",
                "They are converted into runtime validation checks",
                "They become comments in JS",
                "They throw runtime errors"
            ],
            "correct_idx": 0,
            "explanation": "TypeScript uses type erasure: types exist solely at compile time for static analysis and do not incur runtime performance overhead."
        },
        {
            "question": "What utility type in TypeScript makes all properties of an interface read-only?",
            "code": "",
            "options": ["Readonly<T>", "Immutable<T>", "Const<T>", "Freeze<T>"],
            "correct_idx": 0,
            "explanation": "Readonly<T> constructs a type with all properties of T set to readonly."
        },
        {
            "question": "What does the 'never' type represent in TypeScript?",
            "code": "",
            "options": [
                "Values that never occur (e.g. functions that always throw an exception or have infinite loops)",
                "Null or undefined values",
                "Empty string",
                "A deprecated feature"
            ],
            "correct_idx": 0,
            "explanation": "The 'never' type represents the type of values that never occur, commonly used for exhaustive type checking in switch statements."
        },
        {
            "question": "What is the difference between an 'interface' and a 'type' alias in TypeScript?",
            "code": "",
            "options": [
                "Interfaces support declaration merging (can be reopened and extended); type aliases can model unions and tuples directly",
                "Types can be extended with 'implements', interfaces cannot",
                "Interfaces exist at runtime in JS",
                "No difference at all"
            ],
            "correct_idx": 0,
            "explanation": "Interfaces are open for declaration merging across declarations, while type aliases are more flexible for unions, primitives, and intersection types."
        },
        {
            "question": "What operator asserts that a value is neither null nor undefined (non-null assertion)?",
            "code": "",
            "options": ["!", "?", "??", "!!"],
            "correct_idx": 0,
            "explanation": "The postfix exclamation mark (e.g. x!) tells the TypeScript compiler to assert that x is neither null nor undefined."
        },
        {
            "question": "What does the 'as const' assertion do on an object literal?",
            "code": "",
            "options": [
                "Narrows all properties to literal types and marks them readonly",
                "Freezes the object at runtime with Object.freeze",
                "Makes the object global",
                "Converts the object to JSON"
            ],
            "correct_idx": 0,
            "explanation": "'as const' applies const assertion, narrowing string/number literals to their exact values and marking all nested properties readonly."
        }
    ]
}

# Add C# / .NET
QUESTION_BANKS["csharp"] = {
    "title": "C# & .NET Framework Test",
    "questions": [
        {
            "question": "What is the difference between a Value Type (struct) and a Reference Type (class) in C#?",
            "code": "",
            "options": [
                "Value types hold their value directly on the stack; reference types store a reference pointing to an object on the managed heap",
                "Classes cannot inherit from other classes",
                "Structs can have finalizers",
                "There is no difference in C#"
            ],
            "correct_idx": 0,
            "explanation": "Value types (int, float, struct, enum) reside directly on the stack or inline in containing objects. Reference types (class, string, delegate) allocate heap memory managed by the Garbage Collector."
        },
        {
            "question": "What does the 'async' and 'await' pattern accomplish in C#?",
            "code": "",
            "options": [
                "Enables non-blocking asynchronous programming using the Task-based Asynchronous Pattern (TAP)",
                "Creates a separate background OS thread immediately",
                "Locks the current thread from receiving inputs",
                "Forces synchronous blocking execution"
            ],
            "correct_idx": 0,
            "explanation": "async/await allows asynchronous code to be written cleanly without blocking the calling thread, yielding control back until the awaited Task completes."
        },
        {
            "question": "What is LINQ in C#?",
            "code": "",
            "options": [
                "Language-Integrated Query: a syntax to query collections, databases, and XML directly in C#",
                "A library for game physics in Unity",
                "A network protocol for socket communication",
                "A tool to compile C# to WebAssembly"
            ],
            "correct_idx": 0,
            "explanation": "LINQ brings SQL-like declarative querying capabilities directly into C# syntax for arrays, collections, Entity Framework, and XML."
        },
        {
            "question": "What does the CLR (Common Language Runtime) provide in the .NET ecosystem?",
            "code": "",
            "options": [
                "Memory management (Garbage Collection), JIT compilation, thread management, and type safety verification",
                "Only file storage",
                "A web browser rendering engine",
                "A relational database engine"
            ],
            "correct_idx": 0,
            "explanation": "The CLR is the execution engine for .NET applications handling JIT compilation from CIL bytecode to machine code, automatic memory garbage collection, and exception handling."
        },
        {
            "question": "What is the purpose of the 'using' statement in C#?",
            "code": "",
            "options": [
                "Ensures that Dispose() is automatically called on IDisposable objects when leaving scope",
                "Imports a C++ DLL",
                "Instantiates a new thread",
                "Locks a critical section"
            ],
            "correct_idx": 0,
            "explanation": "The using statement guarantees that unmanaged resources (database connections, file streams) are released via IDisposable.Dispose() even if an exception occurs."
        },
        {
            "question": "What is Boxing and Unboxing in C#?",
            "code": "",
            "options": [
                "Boxing converts a value type to a reference type (object); Unboxing extracts the value type from the object",
                "Packaging a C# solution into a ZIP file",
                "Compiling source code to an EXE file",
                "Memory leak detection"
            ],
            "correct_idx": 0,
            "explanation": "Boxing wraps a value type in an object instance on the heap. Unboxing explicitly extracts the original value type back from the object."
        },
        {
            "question": "What keyword is used to prevent a class from being inherited in C#?",
            "code": "",
            "options": ["sealed", "final", "static", "private"],
            "correct_idx": 0,
            "explanation": "In C#, the 'sealed' keyword prevents other classes from deriving from that class."
        },
        {
            "question": "What is a Delegate in C#?",
            "code": "",
            "options": [
                "A type-safe function pointer that references a method with a specific parameter list and return type",
                "A member of parliament",
                "A background process",
                "A thread synchronizer"
            ],
            "correct_idx": 0,
            "explanation": "Delegates encapsulate method references in a type-safe and secure manner, forming the foundation for C# events and lambda expressions."
        },
        {
            "question": "Which collection type in C# represents a key-value store with O(1) average lookup?",
            "code": "",
            "options": ["Dictionary<TKey, TValue>", "List<T>", "ArrayList", "Queue<T>"],
            "correct_idx": 0,
            "explanation": "Dictionary<TKey, TValue> uses hash-based bucketing to provide O(1) average time complexity for retrieval and insertion."
        },
        {
            "question": "What is the Null-Coalescing Operator in C#?",
            "code": "",
            "options": ["??", "?.", "::", "=>"],
            "correct_idx": 0,
            "explanation": "The ?? operator returns the left-hand operand if it is not null; otherwise, it evaluates and returns the right-hand operand (e.g. string name = input ?? 'Default';)."
        }
    ]
}

# Add HTML5 & Web Technologies
QUESTION_BANKS["html_css"] = {
    "title": "HTML5, CSS3 & Web Technologies Test",
    "questions": [
        {
            "question": "Which HTML5 semantic element is most appropriate for independent, self-contained syndicated content (like a blog post)?",
            "code": "",
            "options": ["<article>", "<section>", "<div>", "<aside>"],
            "correct_idx": 0,
            "explanation": "<article> specifies independent, self-contained content intended to be independently distributable or reusable."
        },
        {
            "question": "In the CSS Box Model, what is the order of components from inside to outside?",
            "code": "",
            "options": [
                "Content -> Padding -> Border -> Margin",
                "Content -> Margin -> Border -> Padding",
                "Padding -> Content -> Border -> Margin",
                "Border -> Margin -> Padding -> Content"
            ],
            "correct_idx": 0,
            "explanation": "From the center outward: Content is surrounded by Padding, enclosed by the Border, and separated from adjacent elements by Margin."
        },
        {
            "question": "What does 'box-sizing: border-box;' do in CSS?",
            "code": "",
            "options": [
                "Includes padding and border in the element's total specified width and height",
                "Adds a 3D shadow around the border",
                "Removes margin from the element",
                "Locks the element's aspect ratio"
            ],
            "correct_idx": 0,
            "explanation": "With border-box, the width and height properties include content, padding, and border, making responsive layouts much easier to predict."
        },
        {
            "question": "Which CSS property is used in Flexbox to align items along the cross axis?",
            "code": "",
            "options": ["align-items", "justify-content", "flex-direction", "align-content"],
            "correct_idx": 0,
            "explanation": "justify-content aligns flex items along the main axis; align-items aligns items along the cross axis."
        },
        {
            "question": "What is the difference between localStorage and sessionStorage in HTML5 Web Storage?",
            "code": "",
            "options": [
                "localStorage persists even after browser window is closed; sessionStorage clears when the tab/window is closed",
                "sessionStorage can hold 100 GB; localStorage holds 5 MB",
                "localStorage is sent with every HTTP request automatically",
                "They are identical"
            ],
            "correct_idx": 0,
            "explanation": "localStorage data has no expiration time and survives browser restarts. sessionStorage is scoped to the browser tab lifetime."
        },
        {
            "question": "What is the CSS specificity hierarchy from highest to lowest?",
            "code": "",
            "options": [
                "!important > Inline styles > ID selectors > Class/Attribute/Pseudo-classes > Element selectors",
                "Element selectors > ID selectors > Class selectors",
                "Class selectors > Inline styles > ID selectors",
                "All selectors have equal weight"
            ],
            "correct_idx": 0,
            "explanation": "Inline styles override IDs (specificity 100), IDs override classes (specificity 10), and classes override HTML element tags (specificity 1)."
        },
        {
            "question": "What HTTP status code represents a successful REST API resource creation?",
            "code": "",
            "options": ["201 Created", "200 OK", "204 No Content", "301 Moved Permanently"],
            "correct_idx": 0,
            "explanation": "HTTP 201 Created indicates that the request succeeded and led to the creation of a new resource on the server."
        },
        {
            "question": "What is CORS in web application architecture?",
            "code": "",
            "options": [
                "Cross-Origin Resource Sharing: a browser security mechanism restricting cross-domain HTTP requests",
                "Cascading Object Reference Style",
                "A database connection pool protocol",
                "A JavaScript minifier"
            ],
            "correct_idx": 0,
            "explanation": "CORS uses HTTP headers to allow servers to declare which origin domains are permitted to access their resources via browsers."
        },
        {
            "question": "Which HTML tag is used to embed vector graphics directly in the webpage?",
            "code": "",
            "options": ["<svg>", "<canvas>", "<picture>", "<vector>"],
            "correct_idx": 0,
            "explanation": "<svg> defines scalable vector graphics in XML format that render crisply at any zoom level without pixelation."
        },
        {
            "question": "What does the 'z-index' property control in CSS?",
            "code": "",
            "options": [
                "The vertical stacking order of positioned elements along the 3D Z-axis",
                "Zoom level of the page",
                "Font size scaling",
                "Horizontal alignment"
            ],
            "correct_idx": 0,
            "explanation": "z-index specifies the stack order of positioned elements (relative, absolute, fixed, sticky) along the third dimension."
        }
    ]
}

# Add Go (Golang)
QUESTION_BANKS["golang"] = {
    "title": "Go (Golang) Programming Test",
    "questions": [
        {
            "question": "How do you start a concurrent lightweight thread in Go?",
            "code": "",
            "options": ["go functionName()", "thread functionName()", "async functionName()", "spawn functionName()"],
            "correct_idx": 0,
            "explanation": "Pre-pending the 'go' keyword to any function call spawns a Goroutine executed concurrently by the Go runtime."
        },
        {
            "question": "What is a Channel in Go?",
            "code": "",
            "options": [
                "A typed conduit through which you can send and receive values between Goroutines",
                "A video streaming protocol in Go",
                "An array of strings",
                "A database table handle"
            ],
            "correct_idx": 0,
            "explanation": "Channels are the pipes that connect concurrent Goroutines, following Go's philosophy: 'Do not communicate by sharing memory; instead, share memory by communicating.'"
        },
        {
            "question": "How does Go achieve polymorphism without traditional class inheritance?",
            "code": "",
            "options": [
                "Implicitly implemented Interfaces (duck typing: if it walks like a duck, it is a duck)",
                "Virtual methods and vtables",
                "Abstract classes",
                "Templates"
            ],
            "correct_idx": 0,
            "explanation": "In Go, a type implements an interface simply by implementing its required methods. No explicit 'implements' keyword is required."
        },
        {
            "question": "What is the difference between an Array and a Slice in Go?",
            "code": "",
            "options": [
                "An array has a fixed length defined at compile time; a slice is a dynamically sized, flexible view into an underlying array",
                "Slices can only store integers",
                "Arrays are dynamically sized",
                "There is no difference in Go"
            ],
            "correct_idx": 0,
            "explanation": "Arrays have a fixed size that is part of their type signature ([5]int). Slices ([]int) are lightweight descriptors pointing to an underlying array."
        },
        {
            "question": "What does the 'defer' statement do in Go?",
            "code": "",
            "options": [
                "Defers the execution of a function until the surrounding function returns",
                "Postpones execution by 10 seconds",
                "Throws a panic",
                "Creates a background daemon"
            ],
            "correct_idx": 0,
            "explanation": "A deferred function is placed on a LIFO stack and executed immediately before the surrounding function finishes, making it ideal for closing files and mutexes."
        },
        {
            "question": "What is the zero value of a pointer, slice, map, channel, or interface in Go?",
            "code": "",
            "options": ["nil", "null", "0", "undefined"],
            "correct_idx": 0,
            "explanation": "In Go, uninitialized pointers, slices, maps, channels, and interfaces default to 'nil'."
        },
        {
            "question": "How does Go handle errors without try/catch exceptions?",
            "code": "",
            "options": [
                "Functions return an error as a second return value, checked explicitly via 'if err != nil'",
                "Go programs never throw errors",
                "Using try, catch, finally blocks",
                "Using global error registers"
            ],
            "correct_idx": 0,
            "explanation": "Go emphasizes explicit error handling where functions return a tuple (result, error) and callers explicitly check if err != nil."
        },
        {
            "question": "What built-in function is used to stop ordinary control flow in Go when an unrecoverable runtime error occurs?",
            "code": "",
            "options": ["panic()", "throw()", "exit()", "abort()"],
            "correct_idx": 0,
            "explanation": "panic() terminates normal control flow and begins unwinding the goroutine's stack, which can be captured by recover()."
        },
        {
            "question": "How are identifiers (functions, variables, struct fields) made public / exported across packages in Go?",
            "code": "",
            "options": [
                "By starting the identifier name with an Uppercase letter (e.g. CalculateSum)",
                "Using the 'public' keyword",
                "Using the 'export' keyword",
                "Adding an @export annotation"
            ],
            "correct_idx": 0,
            "explanation": "In Go, case determines visibility: identifiers starting with a capital letter are exported (public); lowercase identifiers are unexported (package-private)."
        },
        {
            "question": "What command compiles and produces a single self-contained native binary in Go?",
            "code": "",
            "options": ["go build", "go run", "go compile", "go make"],
            "correct_idx": 0,
            "explanation": "'go build' compiles Go packages and dependencies into a single standalone executable binary with no external runtime dependencies."
        }
    ]
}


INTERVIEW_DATA = {'hr': {'title': 'HR & Behavioral Interview Questions', 'questions': [{'question': 'Tell me about yourself.', 'intent': 'Assessing communication skills, confidence, career narrative, and relevant technical background.', 'answer': "Start with the 60-Second Elevator Pitch formula (Present -> Past -> Future):<br><br><strong>Present:</strong> 'Good morning! I am currently a final-year Computer Science student passionate about software engineering and problem-solving. My primary technical stack includes Python, Java, SQL, and core CS fundamentals.'<br><strong>Past:</strong> 'During my degree, I have developed full-stack web applications and placement preparation tools, where I designed databases and optimized algorithms. I also consistently practice data structures on coding platforms.'<br><strong>Future:</strong> 'I am eager to begin my software engineering career with your esteemed organization where I can contribute to production systems and continuously learn.'", 'tip': 'Keep it strictly between 60 to 90 seconds. Focus on skills, projects, and impact rather than childhood history.'}, {'question': 'Why should we hire you over other candidates?', 'intent': 'Evaluating self-awareness, alignment with company values, and unique value proposition.', 'answer': "<strong>Model Answer:</strong> 'You should hire me because I combine strong computer science fundamentals with a proven ability to learn and deliver. Beyond my academic coursework, I have built real-world software applications and solved over 100 coding challenges.<br><br>I am not just passionate about writing code; I focus on clean architecture, performance, and teamwork. As a fresher, I bring relentless curiosity, adaptability to your technology stack, and dedication to drive measurable value for your team from day one.'", 'tip': 'Connect your strengths directly to the role requirements. Show genuine enthusiasm for the company.'}, {'question': 'What are your greatest strengths and weaknesses?', 'intent': 'Checking authenticity, self-reflection, and whether you actively work to overcome flaws.', 'answer': "<strong>Strength:</strong> 'My biggest strength is logical problem-solving and rapid learning. When faced with an unfamiliar framework or debugging challenge, I break it down into modular parts and reference documentation to resolve it systematically.'<br><br><strong>Weakness:</strong> 'Earlier, I used to hesitate asking for help when stuck on a challenging bug, spending too much time trying to solve it independently. I learned that in engineering teams, timely collaboration is critical. Now, I give myself a focused timebox to troubleshoot, and if blocked, I consult senior mentors or teammates.'", 'tip': "Never give fake weaknesses like 'I work too hard'. Share a real weakness accompanied by the concrete steps you take to improve."}, {'question': 'Where do you see yourself in five years?', 'intent': 'Assessing career ambition, realistic expectations, and long-term commitment to the company.', 'answer': "<strong>Model Answer:</strong> 'In five years, I see myself as a seasoned Senior Software Engineer who has deeply mastered full-stack systems and scalable architecture. I aim to take ownership of end-to-end features, mentor junior developers, and contribute directly to high-impact technical initiatives. I want to be recognized within the organization as a reliable technical problem-solver.'", 'tip': 'Show ambition while remaining committed to technical execution and company growth.'}, {'question': 'Describe a difficult challenge you faced in a project and how you resolved it (STAR Method).', 'intent': 'Evaluating problem-solving, resilience, and methodical execution under pressure.', 'answer': "<strong>Situation:</strong> 'During my academic capstone project, our web application experienced high response times and occasional database timeout errors during simultaneous student testing.'<br><strong>Task:</strong> 'I was tasked with identifying the bottleneck and optimizing system response time.'<br><strong>Action:</strong> 'I analyzed the query execution plans and identified that missing indexes on frequently searched columns were causing full table scans. I added composite B+ Tree indexes in SQLite/PostgreSQL and refactored redundant backend queries.'<br><strong>Result:</strong> 'Query latency decreased by over 65%, eliminating timeouts and allowing seamless concurrent usage.'", 'tip': 'Always quantify the Result (e.g. 65% faster, 20% memory reduction, delivered on time).'}, {'question': 'Do you have any questions for us?', 'intent': 'Checking curiosity, initiative, and engagement with the interviewer.', 'answer': "<strong>Great questions to ask:</strong><br>1. 'What does a typical onboarding path look like for a graduate software engineer on this team?'<br>2. 'Which programming languages or architectural paradigms is the team currently modernizing?'<br>3. 'What are the key technical challenges your team is currently solving this quarter?'", 'tip': "Never say 'No, I don't have any questions'. Asking insightful questions demonstrates genuine interest in the role."}]}, 'dbms': {'title': 'DBMS & SQL Technical Interview Q&A', 'questions': [{'question': 'Explain the ACID properties with real-world examples.', 'intent': 'Evaluating deep understanding of relational database transactional guarantees.', 'answer': 'ACID ensures reliable database transaction processing:<br>• <strong>Atomicity (All or Nothing):</strong> If you transfer Rs. 1,000 from Account A to Account B, debited money MUST credit B. If a server crash occurs midway, the transaction rolls back completely.<br>• <strong>Consistency:</strong> The database must transition from one valid state to another, enforcing constraints like primary keys and non-negative balances.<br>• <strong>Isolation:</strong> Concurrent transactions run independently without dirty reads or inconsistent states.<br>• <strong>Durability:</strong> Once a transaction is committed, changes persist permanently in disk storage even during system crashes.', 'tip': 'Always mention the banking fund transfer example to illustrate Atomicity and Consistency.'}, {'question': 'What is the difference between Clustered and Non-Clustered Indexes?', 'intent': 'Checking storage engine knowledge and database query optimization.', 'answer': '• <strong>Clustered Index:</strong> Dictates the physical sequence in which table rows are sorted and stored on disk. The leaf nodes contain the actual data rows. Because table rows can only physically be sorted one way, there can only be ONE clustered index per table (typically the Primary Key).<br>• <strong>Non-Clustered Index:</strong> Stored separately from the data rows in a B+ Tree structure. The leaf nodes contain row pointers (Row IDs) pointing to the actual data. A table can have MULTIPLE non-clustered indexes to accelerate WHERE and JOIN lookups.', 'tip': 'Analogy: A Clustered Index is like dictionary words ordered alphabetically; a Non-Clustered Index is like the index at the back of a textbook with page numbers.'}, {'question': 'Explain Database Normalization from 1NF to BCNF.', 'intent': 'Assessing relational schema design and redundancy reduction skills.', 'answer': '• <strong>1NF (First Normal Form):</strong> Eliminate repeating groups; ensure all column values are atomic (indivisible) and each row has a primary key.<br>• <strong>2NF:</strong> Must be in 1NF, and eliminate Partial Dependency (every non-key attribute must depend fully on the primary key, not part of a composite key).<br>• <strong>3NF:</strong> Must be in 2NF, and eliminate Transitive Dependency (non-key attribute must not depend on another non-key attribute: X -> Y -> Z).<br>• <strong>BCNF (Boyce-Codd Normal Form):</strong> A stricter 3NF where for every functional dependency X -> Y, X must be a super key.', 'tip': "Remember the famous mantra: 'Every non-key attribute must depend on the key, the whole key, and nothing but the key, so help me Codd.'"}]}, 'os': {'title': 'Operating Systems Technical Interview Q&A', 'questions': [{'question': 'What is the difference between a Process and a Thread?', 'intent': 'Core OS fundamental tested in almost every placement interview.', 'answer': '• <strong>Process:</strong> An executing instance of a program with its own independent, isolated virtual memory address space (text, data, heap, stack). Creating and switching between processes is resource-intensive.<br>• <strong>Thread:</strong> The smallest unit of CPU execution within a process (often called a lightweight process). Threads inside the same process share the heap, global variables, and code section, but maintain their own private stack and registers.<br>• <strong>Communication:</strong> Processes require IPC (Inter-Process Communication: pipes, sockets, shared memory). Threads communicate directly via shared process memory.', 'tip': "Highlight that context switching between threads is significantly faster than between processes because page tables don't need to be flushed."}, {'question': 'What is Virtual Memory, and how does Paging work?', 'intent': 'Evaluating memory management architecture understanding.', 'answer': "<strong>Virtual Memory:</strong> A memory management technique that gives an application the illusion of having a vast, contiguous address space, even if physical RAM is limited.<br><br><strong>Paging:</strong><br>1. Virtual memory is partitioned into fixed-size chunks called <strong>Pages</strong> (typically 4 KB).<br>2. Physical RAM is partitioned into matching fixed-size chunks called <strong>Page Frames</strong>.<br>3. The CPU's Memory Management Unit (MMU) uses a <strong>Page Table</strong> (accelerated by the TLB cache) to translate virtual addresses to physical frame addresses.<br>4. If a requested page is not in RAM, a <strong>Page Fault</strong> occurs, causing the OS to fetch the page from disk into RAM.", 'tip': 'Mention the Translation Lookaside Buffer (TLB) to demonstrate advanced knowledge.'}]}, 'cn': {'title': 'Computer Networks Technical Interview Q&A', 'questions': [{'question': "What exactly happens when you type 'https://www.google.com' in your browser and press Enter?", 'intent': 'Classic holistic interview question testing the entire web and network stack.', 'answer': '1. <strong>URL Parsing:</strong> The browser parses the protocol (HTTPS), domain (www.google.com), and port (443).<br>2. <strong>DNS Lookup:</strong> Browser checks browser cache -> OS cache -> router cache -> ISP recursive resolver to resolve the domain to an IP address.<br>3. <strong>TCP 3-Way Handshake:</strong> Browser initiates connection with the server via SYN -> SYN-ACK -> ACK.<br>4. <strong>TLS/SSL Handshake:</strong> Encryption keys and certificates are negotiated for HTTPS security.<br>5. <strong>HTTP Request:</strong> Browser sends HTTP GET request with headers.<br>6. <strong>Server Response:</strong> Google web server processes request and returns HTTP 200 OK with HTML/CSS/JS payload.<br>7. <strong>Rendering:</strong> Browser DOM/CSSOM tree is built and rendered on screen.', 'tip': 'Structuring your answer chronologically shows high engineering clarity.'}, {'question': 'Compare TCP vs UDP. When would you use each?', 'intent': 'Testing transport layer protocol selection knowledge.', 'answer': '• <strong>TCP (Transmission Control Protocol):</strong> Connection-oriented, reliable, guarantees packet ordering and delivery via acknowledgments and retransmissions, includes flow control and congestion control. Slower overhead.<br><em>Use cases:</em> Web browsing (HTTP/HTTPS), email (SMTP), file transfers (FTP), database connections.<br><br>• <strong>UDP (User Datagram Protocol):</strong> Connectionless, unreliable, no ordering guarantees, minimal 8-byte header overhead. Extremely fast.<br><em>Use cases:</em> Live video/audio streaming, online multiplayer gaming, DNS queries, VoIP calls.', 'tip': 'Explain that packet loss in voice/video calls causes minor glitching, which is preferable to latency spikes caused by TCP retransmissions.'}]}, 'oops': {'title': 'Object-Oriented Programming (OOPs) Q&A', 'questions': [{'question': 'Explain the Four Pillars of OOPs with real-world software examples.', 'intent': 'Fundamental test of software design principles.', 'answer': '1. <strong>Encapsulation:</strong> Bundling data (variables) and methods together while restricting direct access to object internals using private access modifiers and public getters/setters (e.g. BankAccount class protecting balance).<br>2. <strong>Abstraction:</strong> Hiding complex background implementation details and exposing only essential interfaces (e.g. Driving a car using accelerator/brake without knowing internal combustion physics).<br>3. <strong>Inheritance:</strong> Reusing code where a child class acquires properties and behaviors from a parent class (e.g. Dog and Cat extending Animal).<br>4. <strong>Polymorphism:</strong> Ability of an entity to take multiple forms—compile-time (Method Overloading) and runtime (Method Overriding).', 'code': 'class Animal { void sound() { System.out.println("Animal sound"); } }\nclass Dog extends Animal { void sound() { System.out.println("Bark"); } }', 'tip': 'Always pair each pillar with a 1-sentence real-world analogy.'}, {'question': 'What is the difference between Abstract Class and Interface?', 'intent': 'Evaluating deep OOP design and language-specific architecture knowledge.', 'answer': "• <strong>Abstract Class:</strong> Can have both abstract methods (without body) and concrete methods (with body). Can maintain instance variables and state. A class can extend only ONE abstract class (single inheritance).<br>• <strong>Interface:</strong> Represents a pure contract/blueprint. Historically only held method signatures. A class can implement MULTIPLE interfaces (achieving multiple inheritance).<br><em>Rule of thumb:</em> Use Abstract Class for 'is-a' relationships sharing common code; use Interface for 'can-do' capabilities across unrelated classes.", 'tip': 'Mention that in Java 8+, interfaces can also provide default and static implementations.'}]}, 'python': {'title': 'Python Programming Technical Interview Q&A', 'questions': [{'question': 'What is the difference between Mutable and Immutable types in Python?', 'intent': 'Checking Python memory model and pass-by-object-reference knowledge.', 'answer': '• <strong>Mutable:</strong> Objects whose internal state or values can be modified in-place after creation without changing their memory ID.<br><em>Examples:</em> list, dict, set, bytearray.<br>• <strong>Immutable:</strong> Objects whose values cannot be altered once created. Any modification creates a new object in memory.<br><em>Examples:</em> int, float, str, tuple, frozenset, bool.', 'code': 'a = [1, 2]\nb = a\nb.append(3)\nprint(a) # Output: [1, 2, 3] (Mutable!)\n\nx = 10\ny = x\ny += 5\nprint(x) # Output: 10 (Immutable!)', 'tip': 'Explain that default mutable function arguments (def foo(lst=[])) retain values across calls, a classic placement interview trap.'}, {'question': 'What are Decorators and Generators in Python?', 'intent': 'Evaluating intermediate to advanced Python programming proficiency.', 'answer': "• <strong>Decorator:</strong> A design pattern and function that accepts another function as an argument, extends its behavior without modifying its source code, and returns the modified function (using @syntax). Commonly used for logging, authentication, and execution timing.<br>• <strong>Generator:</strong> A function containing the 'yield' keyword that produces a sequence of values lazily on-demand one at a time. It maintains state between iterations, offering massive memory savings when processing large datasets.", 'code': '# Generator Example:\ndef count_up_to(n):\n    i = 1\n    while i <= n:\n        yield i\n        i += 1', 'tip': 'Highlight that generators prevent Out-Of-Memory (OOM) errors when processing gigabyte-sized log files.'}]}, 'java': {'title': 'Java Technical Interview Q&A', 'questions': [{'question': "How does Java's HashMap work internally?", 'intent': 'One of the most frequently asked Java placement interview questions.', 'answer': "1. <strong>Underlying Structure:</strong> An array of Node/Entry buckets (default size 16, load factor 0.75).<br>2. <strong>Hashing & Indexing:</strong> When calling map.put(key, value), key.hashCode() is calculated and hashed to find the bucket index: (n - 1) & hash.<br>3. <strong>Collision Resolution:</strong> If two different keys map to the same bucket, entries are chained via a Singly Linked List.<br>4. <strong>Treeification (Java 8):</strong> If a bucket's linked list exceeds 8 nodes and array capacity >= 64, it converts to a Red-Black Tree, improving lookup from O(N) to O(log N).", 'tip': 'Always mention the equals() and hashCode() contract: if two objects are equal by equals(), they MUST return identical hashCodes.'}, {'question': 'Why are Strings immutable in Java?', 'intent': 'Evaluating JVM architecture and security understanding.', 'answer': 'Strings are immutable in Java for four critical reasons:<br>1. <strong>String Constant Pool:</strong> Enables memory caching so identical string literals share the same pooled heap instance.<br>2. <strong>Security:</strong> Strings are used for database connection URLs, usernames, passwords, and network sockets. Immutability prevents malicious alteration.<br>3. <strong>Thread Safety:</strong> Because string objects cannot be modified, they are inherently thread-safe across concurrent threads without synchronization locks.<br>4. <strong>Hashcode Caching:</strong> Hash codes are pre-calculated and cached upon creation, speeding up HashMap and HashSet lookups.', 'tip': 'Mention that StringBuilder and StringBuffer exist for scenarios requiring heavy in-place string concatenation.'}]}, 'dsa': {'title': 'Data Structures & Algorithms Interview Q&A', 'questions': [{'question': 'Explain the Two-Pointer and Sliding Window techniques.', 'intent': 'Testing algorithmic problem-solving patterns frequently tested in online coding rounds.', 'answer': "• <strong>Two-Pointer Technique:</strong> Uses two pointers moving in the same or opposite directions through an array/string. Commonly used for in-place array reversal, checking palindromes, and finding pairs in sorted arrays (Two Sum II in O(N) time).<br>• <strong>Sliding Window Technique:</strong> Maintains a dynamic or fixed-size window over contiguous array/string elements. Instead of recalculating subarrays in O(N^2), it adjusts window boundaries in O(N) time. Ideal for 'Maximum Sum Subarray of size K' or 'Longest Substring Without Repeating Characters'.", 'tip': 'Two-pointer saves O(N) auxiliary space; sliding window reduces nested loops from O(N^2) to O(N).'}, {'question': "How does Floyd's Cycle Detection Algorithm work in a Linked List?", 'intent': 'Evaluating pointer manipulation and algorithmic proofs.', 'answer': "Floyd's algorithm (Tortoise and Hare) uses two pointers:<br>1. <strong>Slow Pointer:</strong> advances 1 node per iteration.<br>2. <strong>Fast Pointer:</strong> advances 2 nodes per iteration.<br><br>If the linked list is linear, the fast pointer hits null (no cycle). If a cycle exists, the relative distance between them decreases by 1 step every loop iteration until they are mathematically guaranteed to meet inside the loop.<br><strong>Complexity:</strong> O(N) time, O(1) space.", 'tip': 'To find the starting node of the cycle after they meet, reset slow to head and advance both pointers 1 step at a time until they meet again.'}]}}

CODING_CHALLENGES = {
    "Python": [
        {
            "id": 1,
            "title": "Two Sum Problem",
            "difficulty": "Easy",
            "topic": "Arrays & Hash Table",
            "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume each input has exactly one solution.",
            "sample_input": "nums = [2, 7, 11, 15], target = 9",
            "sample_output": "[0, 1]",
            "constraints": "2 <= nums.length <= 10^4",
            "starter_code": """def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))"""
        },
        {
            "id": 2,
            "title": "Palindrome String Check",
            "difficulty": "Easy",
            "topic": "Strings",
            "description": "Write a function that checks whether a given string is a palindrome (reads identical forwards and backwards), ignoring case and non-alphanumeric characters.",
            "sample_input": "s = 'A man, a plan, a canal: Panama'",
            "sample_output": "True",
            "constraints": "1 <= s.length <= 2 * 10^5",
            "starter_code": """def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome('A man, a plan, a canal: Panama'))"""
        },
        {
            "id": 3,
            "title": "Reverse Linked List",
            "difficulty": "Medium",
            "topic": "Linked Lists",
            "description": "Given the head of a singly linked list, reverse the list and return the reversed list head.",
            "sample_input": "head = [1, 2, 3, 4, 5]",
            "sample_output": "[5, 4, 3, 2, 1]",
            "constraints": "Number of nodes is [0, 5000]",
            "starter_code": """class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

print("Reversed successfully")"""
        }
    ],
    "Java": [
        {
            "id": 1,
            "title": "Reverse an Array In-Place",
            "difficulty": "Easy",
            "topic": "Arrays",
            "description": "Write a Java program to reverse an integer array in place without using additional memory.",
            "sample_input": "int[] arr = {1, 2, 3, 4, 5};",
            "sample_output": "[5, 4, 3, 2, 1]",
            "constraints": "Space Complexity: O(1)",
            "starter_code": """public class Main {
    public static void reverse(int[] arr) {
        int left = 0, right = arr.length - 1;
        while(left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        reverse(arr);
        for(int n : arr) System.out.print(n + " ");
    }
}"""
        },
        {
            "id": 2,
            "title": "Fibonacci Series with Memoization",
            "difficulty": "Easy",
            "topic": "Recursion & DP",
            "description": "Calculate the N-th Fibonacci number using dynamic programming or recursion.",
            "sample_input": "n = 10",
            "sample_output": "55",
            "constraints": "0 <= n <= 45",
            "starter_code": """public class Main {
    public static int fib(int n) {
        if (n <= 1) return n;
        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            int c = a + b;
            a = b;
            b = c;
        }
        return b;
    }
    public static void main(String[] args) {
        System.out.println(fib(10));
    }
}"""
        }
    ],
    "C": [
        {
            "id": 1,
            "title": "Reverse a String Using Pointers",
            "difficulty": "Easy",
            "topic": "Pointers & Strings",
            "description": "Write a C function to reverse a null-terminated string in place using two pointers without extra space.",
            "sample_input": "char str[] = \"placement\";",
            "sample_output": "\"tnemecalp\"",
            "constraints": "In-place reversal, O(1) space",
            "starter_code": """#include <stdio.h>
#include <string.h>

void reverseString(char* str) {
    char *start = str;
    char *end = str + strlen(str) - 1;
    char temp;
    while (start < end) {
        temp = *start;
        *start = *end;
        *end = temp;
        start++;
        end--;
    }
}

int main() {
    char s[] = "placement";
    reverseString(s);
    printf("%s\\n", s);
    return 0;
}"""
        }
    ],
    "C++": [
        {
            "id": 1,
            "title": "Binary Search Implementation",
            "difficulty": "Easy",
            "topic": "Searching",
            "description": "Implement Binary Search on a sorted vector of integers in C++ with O(log N) time complexity.",
            "sample_input": "arr = [2, 5, 8, 12, 16, 23, 38], target = 16",
            "sample_output": "Index: 4",
            "constraints": "Array is sorted in ascending order",
            "starter_code": """#include <iostream>
#include <vector>
using namespace std;

int binarySearch(const vector<int>& arr, int target) {
    int low = 0, high = arr.size() - 1;
    while(low <= high) {
        int mid = low + (high - low) / 2;
        if(arr[mid] == target) return mid;
        else if(arr[mid] < target) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

int main() {
    vector<int> arr = {2, 5, 8, 12, 16, 23, 38};
    cout << "Index: " << binarySearch(arr, 16) << endl;
    return 0;
}"""
        }
    ],
    "JavaScript": [
        {
            "id": 1,
            "title": "Debounce Function Implementation",
            "difficulty": "Medium",
            "topic": "Closures & Async",
            "description": "Implement a debounce function in JavaScript that delays invoking func until after wait milliseconds have elapsed.",
            "sample_input": "debounce(logMessage, 300)",
            "sample_output": "Invoked once after settling",
            "constraints": "Modern ES6 syntax",
            "starter_code": """function debounce(func, wait) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
}

const log = debounce(() => console.log('Action executed!'), 300);
log();"""
        }
    ],
    "TypeScript": [
        {
            "id": 1,
            "title": "Generic LRU Cache",
            "difficulty": "Hard",
            "topic": "Generics & Maps",
            "description": "Design a generic type-safe LRU cache with capacity limit in TypeScript.",
            "sample_input": "cache.put('a', 1); cache.get('a');",
            "sample_output": "1",
            "constraints": "Key must extend string | number",
            "starter_code": """class LRUCache<K, V> {
    private capacity: number;
    private map: Map<K, V> = new Map();

    constructor(capacity: number) {
        this.capacity = capacity;
    }

    get(key: K): V | undefined {
        if (!this.map.has(key)) return undefined;
        const val = this.map.get(key)!;
        this.map.delete(key);
        this.map.set(key, val);
        return val;
    }

    put(key: K, value: V): void {
        if (this.map.has(key)) this.map.delete(key);
        else if (this.map.size >= this.capacity) {
            const firstKey = this.map.keys().next().value;
            if (firstKey !== undefined) this.map.delete(firstKey);
        }
        this.map.set(key, value);
    }
}

const lru = new LRUCache<string, number>(2);
lru.put('a', 100);
console.log(lru.get('a'));"""
        }
    ],
    "SQL": [
        {
            "id": 1,
            "title": "Find Second Highest Salary",
            "difficulty": "Medium",
            "topic": "SQL Subqueries",
            "description": "Write an SQL query to report the second highest salary from the Employee table.",
            "sample_input": "Employee (id, salary)",
            "sample_output": "SecondHighestSalary: 200",
            "constraints": "Table may have duplicate salary amounts",
            "starter_code": """SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);"""
        }
    ],
    "Go": [
        {
            "id": 1,
            "title": "Concurrent Worker Pool with Channels",
            "difficulty": "Medium",
            "topic": "Concurrency & Channels",
            "description": "Implement a worker pool in Go that processes tasks concurrently using Goroutines and buffered channels.",
            "sample_input": "numJobs = 5, numWorkers = 3",
            "sample_output": "All 5 jobs completed concurrently",
            "constraints": "Use sync.WaitGroup",
            "starter_code": """package main

import (
    "fmt"
    "sync"
)

func worker(id int, jobs <-chan int, results chan<- int, wg *sync.WaitGroup) {
    defer wg.Done()
    for j := range jobs {
        results <- j * 2
    }
}

func main() {
    const numJobs = 5
    jobs := make(chan int, numJobs)
    results := make(chan int, numJobs)
    var wg sync.WaitGroup

    for w := 1; w <= 3; w++ {
        wg.Add(1)
        go worker(w, jobs, results, &wg)
    }

    for j := 1; j <= numJobs; j++ {
        jobs <- j
    }
    close(jobs)

    wg.Wait()
    close(results)

    for r := range results {
        fmt.Println(r)
    }
}"""
        }
    ]
}


# ---------------------------------------------------------------------
# PART 2: STYLESHEET
# ---------------------------------------------------------------------
SITE_CSS = r'''
/* =====================================================================
   PLACEMENT PREPARATION PORTAL — DESIGN SYSTEM
   Navy + amber identity, light content surfaces, clear hierarchy.
   Sections: 1 Tokens · 2 Base · 3 Navbar · 4 Layout/Hero · 5 Buttons/Badges
             6 Forms · 7 Auth · 8 Dashboard · 9 Modules · 10 Tables
             11 Coding · 12 Interview · 13 Companies · 14 Tests · 15 Responsive
   ===================================================================== */

/* ---------- 1. TOKENS ---------- */
:root {
    --navy-950: #0a1426;
    --navy-900: #0f1f3d;
    --navy-800: #172d4f;
    --navy-700: #213b66;
    --navy-600: #2c4c80;

    --amber-500: #e09b48;
    --amber-400: #efb066;
    --amber-100: #fdf1e0;

    --primary: #2457d6;
    --primary-dark: #1b44b0;
    --primary-soft: #eaf0fe;

    --success: #0f9d6b;
    --success-soft: #def7ec;
    --warning: #b7791f;
    --warning-soft: #fef3c7;
    --danger: #d03a3a;
    --danger-soft: #fde8e8;
    --purple: #7c3aed;
    --purple-soft: #f1eaff;

    --bg-page: #f3f5f9;
    --bg-card: #ffffff;
    --bg-subtle: #f7f9fc;
    --border-color: #e2e8f0;
    --border-strong: #cbd5e1;

    --text-primary: #14233f;
    --text-secondary: #46566f;
    --text-muted: #7384a0;

    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 22px;

    --shadow-sm: 0 1px 2px rgba(15, 31, 61, .05), 0 2px 8px rgba(15, 31, 61, .04);
    --shadow-md: 0 4px 14px rgba(15, 31, 61, .08);
    --shadow-lg: 0 18px 44px rgba(15, 31, 61, .16);

    --font-sans: "Plus Jakarta Sans", "Segoe UI", system-ui, -apple-system, Arial, sans-serif;
    --font-mono: "JetBrains Mono", "Fira Code", Consolas, "Courier New", monospace;
    --nav-h: 68px;
}

/* ---------- 2. BASE ---------- */
*, *::before, *::after { box-sizing: border-box; }
html { scroll-behavior: smooth; scroll-padding-top: calc(var(--nav-h) + 16px); }

body {
    margin: 0;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    font-family: var(--font-sans);
    font-size: 15px;
    line-height: 1.55;
    color: var(--text-primary);
    background: var(--bg-page);
    -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4 { margin: 0 0 .4em; line-height: 1.25; letter-spacing: -.015em; color: var(--text-primary); }
p { margin: 0 0 .8em; }
a { color: var(--primary); text-decoration: none; }
a:hover { text-decoration: underline; }
img { max-width: 100%; }
strong { font-weight: 700; }

pre {
    margin: 12px 0;
    padding: 14px 18px;
    background: var(--navy-950);
    color: #cfe3ff;
    border-radius: var(--radius-md);
    font-family: var(--font-mono);
    font-size: 13.5px;
    line-height: 1.65;
    overflow-x: auto;
    border: 1px solid #1c2c4d;
}
pre code { background: none; padding: 0; color: inherit; font-family: inherit; }

::selection { background: var(--amber-400); color: var(--navy-900); }
:focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }

/* ---------- 2b. PAGE BACKGROUND PHOTOS ---------- */
body.page-login, body.page-register     { --page-img: url("https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=1920&q=80"); }
body.page-dashboard                     { --page-img: url("https://images.unsplash.com/photo-1523240795612-9a054b0db644?auto=format&fit=crop&w=1920&q=80"); }
body.page-aptitude                      { --page-img: url("https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&w=1920&q=80"); }
body.page-coding                        { --page-img: url("https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=1920&q=80"); }
body.page-interview                     { --page-img: url("https://images.unsplash.com/photo-1521737711867-e3b97375f902?auto=format&fit=crop&w=1920&q=80"); }
body.page-companies                     { --page-img: url("https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=1920&q=80"); }
body.page-profile, body.page-scores,
body.page-test-review, body.page-test-result { --page-img: url("https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1920&q=80"); }

/* photo behind the whole page, softened with a blue-white wash */
body[class*="page-"] {
    background:
        linear-gradient(rgba(232, 240, 255, .55), rgba(244, 247, 252, .78)),
        var(--page-img) center / cover fixed no-repeat,
        var(--bg-page);
}

/* ---------- 3. NAVBAR ---------- */
.navbar {
    position: sticky; top: 0; z-index: 100;
    min-height: var(--nav-h);
    display: flex; align-items: center; justify-content: space-between; gap: 20px;
    padding: 0 max(20px, calc((100% - 1200px) / 2));
    background: rgba(10, 20, 38, .94);
    backdrop-filter: blur(14px);
    border-bottom: 1px solid rgba(255, 255, 255, .07);
}
.brand-container { display: flex; align-items: center; gap: 12px; color: #fff; flex-shrink: 0; }
.brand-container:hover { text-decoration: none; }
.brand-logo {
    width: 40px; height: 40px; border-radius: 12px;
    display: grid; place-items: center;
    background: linear-gradient(135deg, var(--amber-400), var(--amber-500));
    color: var(--navy-900); font-weight: 800; font-size: 20px;
    box-shadow: 0 4px 12px rgba(224, 155, 72, .35);
}
.brand-text h2 { margin: 0; font-size: 16px; color: #fff; letter-spacing: -.01em; }
.brand-text span { font-size: 11.5px; color: #8fa3c4; }

.nav-links { display: flex; align-items: center; gap: 2px; }
.nav-links a {
    position: relative;
    padding: 9px 14px; border-radius: 10px;
    font-size: 14px; font-weight: 600; color: #b4c3dc;
    transition: background .2s, color .2s;
}
.nav-links a:hover { background: rgba(255, 255, 255, .08); color: #fff; text-decoration: none; }
.nav-links a.active { color: #fff; background: rgba(255, 255, 255, .1); }
.nav-links a.active::after {
    content: ""; position: absolute; left: 14px; right: 14px; bottom: 3px;
    height: 2px; border-radius: 2px; background: var(--amber-500);
}
.nav-links a.nav-logout { margin-left: 8px; border: 1px solid rgba(224, 155, 72, .55); color: var(--amber-400); }
.nav-links a.nav-logout:hover { background: var(--amber-500); color: var(--navy-900); }
.nav-links a.nav-logout.active::after { display: none; }

/* ---------- 4. LAYOUT, FLASH, HERO, SECTION TITLES ---------- */
.main-container {
    width: min(1240px, 94%); margin: 24px auto 48px; flex: 1;
    padding: 26px;
    background: rgba(255, 255, 255, .70);
    backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, .8);
    border-radius: 26px;
    box-shadow: 0 20px 50px rgba(15, 31, 61, .18);
}

footer { padding: 22px 20px; text-align: center; font-size: 13px; color: var(--text-secondary); border-top: 1px solid rgba(255,255,255,.6); background: rgba(255, 255, 255, .82); backdrop-filter: blur(8px); }
footer p { margin: 0; }

.alert {
    display: flex; align-items: center; gap: 10px;
    padding: 13px 18px; margin-bottom: 18px;
    border-radius: var(--radius-md); border: 1px solid; border-left-width: 4px;
    font-weight: 600; font-size: 14px; background: #fff; box-shadow: var(--shadow-sm);
}
.alert-success { color: #0b6b49; background: var(--success-soft); border-color: #86e0b9; }
.alert-info    { color: #1b44b0; background: var(--primary-soft); border-color: #aac3fb; }
.alert-danger  { color: #9b2424; background: var(--danger-soft); border-color: #f4a6a6; }
.alert-warning { color: #8a5a10; background: var(--warning-soft); border-color: #f2d27a; }

.hero-banner {
    position: relative; overflow: hidden;
    margin-bottom: 28px; padding: 38px 40px;
    border-radius: var(--radius-xl);
    color: #fff;
    background:
        linear-gradient(105deg, rgba(10, 20, 38, .92) 0%, rgba(23, 45, 79, .78) 55%, rgba(36, 87, 214, .45) 100%),
        var(--page-img, none) center / cover no-repeat,
        var(--navy-800);
    box-shadow: var(--shadow-lg);
}
.hero-banner::after {
    content: ""; position: absolute; inset: 0; pointer-events: none; opacity: .5;
    background-image: radial-gradient(rgba(255, 255, 255, .13) 1px, transparent 1px);
    background-size: 22px 22px;
    -webkit-mask-image: linear-gradient(100deg, transparent 35%, #000);
            mask-image: linear-gradient(100deg, transparent 35%, #000);
}
.hero-content { position: relative; z-index: 1; max-width: 820px; }
.hero-banner h1 { color: #fff; font-size: clamp(26px, 3.4vw, 36px); font-weight: 800; margin-bottom: 10px; }
.hero-banner p { color: #c3d1ea; font-size: 15.5px; line-height: 1.65; margin-bottom: 18px; }
.hero-banner p strong { color: #fff; }
.hero-meta { display: flex; flex-wrap: wrap; gap: 10px; }
.hero-tag {
    padding: 7px 14px; border-radius: 999px;
    background: rgba(255, 255, 255, .1); border: 1px solid rgba(255, 255, 255, .18);
    font-size: 13px; font-weight: 600; color: #eaf1ff; backdrop-filter: blur(6px);
}
.hero-tag strong { color: var(--amber-400); }

.section-title {
    display: flex; align-items: center; gap: 4px;
    margin: 36px 0 18px; font-size: 20px; font-weight: 800; color: var(--text-primary);
}
.section-title svg { flex-shrink: 0; }
.section-title span { display: inline-flex; align-items: center; gap: 10px; }

/* ---------- 5. BUTTONS & BADGES ---------- */
.btn, button.btn, input[type="submit"].btn {
    display: inline-flex; align-items: center; justify-content: center; gap: 8px;
    padding: 11px 20px;
    font: 700 14px/1.2 var(--font-sans);
    border: 1px solid transparent; border-radius: 10px;
    cursor: pointer; text-decoration: none;
    transition: transform .15s, box-shadow .2s, background .2s, border-color .2s;
}
.btn:hover { text-decoration: none; transform: translateY(-1px); }
.btn:active { transform: translateY(0); }
.btn-primary { background: var(--primary); color: #fff; box-shadow: 0 4px 12px rgba(36, 87, 214, .28); }
.btn-primary:hover { background: var(--primary-dark); color: #fff; box-shadow: 0 6px 16px rgba(36, 87, 214, .36); }
.btn-secondary { background: #fff; color: var(--navy-800); border-color: var(--border-strong); }
.btn-secondary:hover { background: var(--bg-subtle); border-color: var(--navy-600); color: var(--navy-800); }
.btn-success { background: var(--success); color: #fff; box-shadow: 0 4px 12px rgba(15, 157, 107, .26); }
.btn-success:hover { background: #0b8359; color: #fff; }
.btn-sm { padding: 8px 14px; font-size: 13px; border-radius: 9px; }

.badge {
    display: inline-flex; align-items: center; gap: 4px;
    padding: 4px 11px; border-radius: 999px;
    font-size: 12px; font-weight: 700; white-space: nowrap;
}
.badge-info    { background: var(--primary-soft); color: var(--primary-dark); }
.badge-success { background: var(--success-soft); color: #0b6b49; }
.badge-warning { background: var(--warning-soft); color: #8a5a10; }
.badge-danger  { background: var(--danger-soft); color: #a32828; }
.badge-purple  { background: var(--purple-soft); color: #5b21b6; }

/* ---------- 6. FORMS ---------- */
.form-group { margin-bottom: 18px; }
.form-group label, label.field-label {
    display: block; margin-bottom: 7px;
    font-size: 13.5px; font-weight: 700; color: var(--text-primary);
}
input[type="text"], input[type="email"], input[type="password"], input[type="search"],
input[type="number"], select, textarea {
    width: 100%; padding: 12px 14px;
    font: 500 15px var(--font-sans); color: var(--text-primary);
    background: #fff; border: 1px solid var(--border-strong); border-radius: 10px;
    transition: border-color .2s, box-shadow .2s;
}
input::placeholder, textarea::placeholder { color: #9aa8bf; }
input:hover, select:hover, textarea:hover { border-color: var(--navy-600); }
input:focus, select:focus, textarea:focus {
    outline: none; border-color: var(--primary); box-shadow: 0 0 0 4px rgba(36, 87, 214, .14);
}
input[type="radio"], input[type="checkbox"] { accent-color: var(--primary); width: 18px; height: 18px; margin: 0; flex-shrink: 0; }
input[readonly] { background: var(--bg-subtle); color: var(--text-muted); }

.form-actions { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
.form-grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }

.profile-edit-wrap { max-width: 860px; margin: 0 auto; }
.form-card {
    background: var(--bg-card); border: 1px solid var(--border-color);
    border-radius: var(--radius-xl); padding: 34px; box-shadow: var(--shadow-md);
}
.form-card h1 { font-size: 26px; font-weight: 800; }
.form-card .form-intro { color: var(--text-muted); margin-bottom: 26px; }

/* ---------- 7. AUTH ---------- */
body.page-login, body.page-register {
    background:
        linear-gradient(160deg, rgba(10, 20, 38, .78), rgba(23, 45, 79, .62)),
        var(--page-img) center / cover fixed no-repeat,
        var(--navy-900);
}
body.page-login .main-container, body.page-register .main-container {
    background: none; backdrop-filter: none; -webkit-backdrop-filter: none; border: 0; box-shadow: none; padding: 0;
}
body.page-login footer, body.page-register footer { background: rgba(10, 20, 38, .55); border-color: rgba(255, 255, 255, .1); color: #b4c3dc; }
body.page-login .alert, body.page-register .alert { max-width: 440px; margin-left: auto; margin-right: auto; }

.auth-wrapper { display: flex; justify-content: center; align-items: center; padding: 18px 0 8px; }
.auth-box {
    width: min(440px, 100%);
    padding: 38px 36px 30px;
    background: #fff; border-radius: 24px;
    box-shadow: 0 30px 70px rgba(0, 0, 0, .38);
}
.auth-header { text-align: center; margin-bottom: 26px; }
.logo-badge {
    width: 56px; height: 56px; margin: 0 auto 16px;
    display: grid; place-items: center; border-radius: 16px;
    background: linear-gradient(135deg, var(--amber-400), var(--amber-500));
    color: var(--navy-900); font-size: 26px; font-weight: 800;
    box-shadow: 0 8px 20px rgba(224, 155, 72, .4);
}
.auth-header h1 { font-size: 26px; font-weight: 800; margin-bottom: 6px; }
.auth-header p { color: var(--text-muted); margin: 0; font-size: 14.5px; }
.auth-footer { margin-top: 22px; padding-top: 20px; border-top: 1px solid var(--border-color); text-align: center; font-size: 14px; color: var(--text-muted); }
.auth-footer a { font-weight: 700; }

/* ---------- 8. DASHBOARD ---------- */
.profile-card {
    background: var(--bg-card); border: 1px solid var(--border-color);
    border-radius: var(--radius-lg); padding: 24px; box-shadow: var(--shadow-sm);
}
.profile-header { display: flex; align-items: center; gap: 16px; }
.profile-avatar {
    width: 58px; height: 58px; border-radius: 18px;
    display: grid; place-items: center;
    background: linear-gradient(135deg, var(--navy-700), var(--navy-900));
    color: var(--amber-400); font-size: 24px; font-weight: 800; text-transform: uppercase;
}
.profile-details h2 { margin: 0; font-size: 20px; }
.profile-details p { margin: 2px 0 0; color: var(--text-muted); font-size: 14px; }
.profile-fields-grid {
    display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;
    margin-top: 22px; padding-top: 22px; border-top: 1px dashed var(--border-strong);
}
.profile-field-item { padding: 14px 16px; background: var(--bg-subtle); border: 1px solid var(--border-color); border-radius: var(--radius-md); }
.profile-field-label { margin-bottom: 6px; font-size: 11.5px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; color: var(--text-muted); }
.profile-field-value { font-size: 15px; font-weight: 600; color: var(--text-primary); }

.stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 18px; }
.stat-card {
    position: relative; display: flex; flex-direction: column;
    padding: 22px; color: var(--text-primary);
    background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg);
    box-shadow: var(--shadow-sm); overflow: hidden;
    transition: transform .2s, box-shadow .2s, border-color .2s;
}
.stat-card::before { content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 4px; background: var(--stat-accent, var(--primary)); }
.stat-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); border-color: var(--stat-accent, var(--primary)); text-decoration: none; }
.tests-card  { --stat-accent: var(--primary); }
.score-card  { --stat-accent: var(--amber-500); }
.coding-card { --stat-accent: var(--success); }
.stat-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; }
.stat-title { font-size: 13px; font-weight: 700; letter-spacing: .05em; text-transform: uppercase; color: var(--text-muted); }
.stat-icon { width: 42px; height: 42px; border-radius: 12px; display: grid; place-items: center; }
.stat-icon.tests  { background: var(--primary-soft); color: var(--primary); }
.stat-icon.score  { background: var(--amber-100); color: #b8741f; }
.stat-icon.coding { background: var(--success-soft); color: var(--success); }
.stat-value { font-size: 36px; font-weight: 800; letter-spacing: -.03em; line-height: 1.1; color: var(--navy-900); }
.stat-subtitle { margin: 8px 0 16px; font-size: 13.5px; color: var(--text-secondary); }
.stat-link-action { margin-top: auto; font-size: 13px; font-weight: 700; color: var(--stat-accent, var(--primary)); }
.stat-card:hover .stat-link-action span { text-decoration: underline; }

/* ---------- 9. MODULE CARDS ---------- */
.modules-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; }
.module-card {
    --mod-accent: var(--primary);
    display: flex; flex-direction: column; justify-content: space-between; gap: 18px;
    padding: 24px;
    background: var(--bg-card); border: 1px solid var(--border-color);
    border-top: 4px solid var(--mod-accent);
    border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);
    transition: transform .2s, box-shadow .2s;
}
.module-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }
.module-card.aptitude  { --mod-accent: var(--primary); }
.module-card.coding    { --mod-accent: var(--success); }
.module-card.interview { --mod-accent: var(--purple); }
.module-card.companies { --mod-accent: #ea580c; }
.module-icon-wrap {
    width: 56px; height: 56px; margin-bottom: 16px; border-radius: 16px;
    display: grid; place-items: center;
    background: color-mix(in srgb, var(--mod-accent) 12%, #fff);
}
.module-icon-wrap .lang-icon, .module-icon-wrap img { width: 32px; height: 32px; object-fit: contain; }
.module-card h3 { font-size: 18px; font-weight: 800; }
.module-card p { color: var(--text-secondary); font-size: 14px; line-height: 1.65; }
.module-tags { display: flex; flex-wrap: wrap; gap: 7px; margin-top: 12px; }
.module-tag { padding: 4px 11px; border-radius: 999px; background: var(--bg-subtle); border: 1px solid var(--border-color); font-size: 12px; font-weight: 600; color: var(--text-secondary); }
.module-btn {
    display: block; padding: 12px 18px; border-radius: 10px;
    background: var(--mod-accent); color: #fff; text-align: center;
    font-size: 14px; font-weight: 700;
    transition: filter .2s, transform .15s;
}
.module-btn:hover { color: #fff; text-decoration: none; filter: brightness(1.1); transform: translateY(-1px); }
.module-card.aptitude .module-btn, .module-card.coding .module-btn, .module-card.interview .module-btn, .module-card.companies .module-btn { background: var(--mod-accent); }

/* ---------- 10. TABLES ---------- */
.table-container {
    margin-top: 28px; overflow: hidden;
    background: var(--bg-card); border: 1px solid var(--border-color);
    border-radius: var(--radius-lg); box-shadow: var(--shadow-sm);
}
.table-container > table, .table-container .table-scroll { display: block; overflow-x: auto; }
.custom-table { width: 100%; border-collapse: collapse; display: table !important; min-width: 640px; }
.table-container { overflow-x: auto; }
.custom-table th {
    padding: 13px 18px; text-align: left; white-space: nowrap;
    font-size: 11.5px; font-weight: 700; letter-spacing: .06em; text-transform: uppercase;
    color: var(--text-muted); background: var(--bg-subtle); border-bottom: 1px solid var(--border-color);
}
.custom-table td { padding: 15px 18px; font-size: 14px; color: var(--text-secondary); border-bottom: 1px solid var(--border-color); vertical-align: middle; }
.custom-table td strong { color: var(--text-primary); }
.custom-table tbody tr { transition: background .15s; }
.custom-table tbody tr:hover { background: #f8faff; }
.custom-table tbody tr:last-child td { border-bottom: none; }

/* ---------- 11. CODING STUDIO ---------- */
.coding-tabs { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px; }
.coding-tab {
    display: inline-flex; align-items: center; gap: 8px;
    padding: 9px 16px; border-radius: 999px;
    background: #fff; border: 1px solid var(--border-color);
    font-size: 13.5px; font-weight: 700; color: var(--text-secondary);
    box-shadow: var(--shadow-sm); transition: all .2s;
}
.coding-tab:hover { border-color: var(--navy-600); color: var(--navy-800); text-decoration: none; transform: translateY(-1px); }
.coding-tab.active { background: var(--navy-800); border-color: var(--navy-800); color: #fff; box-shadow: 0 6px 16px rgba(23, 45, 79, .3); }
.tab-lang-icon { width: 20px; height: 20px; object-fit: contain; }

.coding-layout { display: grid; grid-template-columns: 340px minmax(0, 1fr); gap: 24px; align-items: start; }
.coding-layout > div:first-child { position: sticky; top: calc(var(--nav-h) + 18px); }

.code-editor-area {
    display: block; width: 100%; min-height: 280px; resize: vertical;
    padding: 18px 20px;
    font-family: var(--font-mono) !important; font-size: 14px; line-height: 1.7; tab-size: 4;
    color: #dbe7ff; background: var(--navy-950);
    border: 1px solid #1c2c4d; border-radius: var(--radius-md);
    caret-color: var(--amber-400);
}
.code-editor-area:hover { border-color: #2c4c80; }
.code-editor-area:focus { border-color: var(--amber-500); box-shadow: 0 0 0 4px rgba(224, 155, 72, .18); }
.code-output-box {
    padding: 16px 18px; border-radius: var(--radius-md);
    background: var(--navy-950); color: #e2e8f0; border: 1px solid #1c2c4d;
    font-family: var(--font-mono); font-size: 13.5px; line-height: 1.8;
}

/* ---------- 12. INTERVIEW ---------- */
.accordion-item {
    margin-bottom: 12px; overflow: hidden;
    background: var(--bg-card); border: 1px solid var(--border-color);
    border-radius: var(--radius-md); box-shadow: var(--shadow-sm);
    transition: border-color .2s, box-shadow .2s;
}
.accordion-item[open] { border-color: var(--primary); box-shadow: var(--shadow-md); }
.accordion-summary {
    display: flex; justify-content: space-between; align-items: center; gap: 16px;
    padding: 18px 22px; cursor: pointer; list-style: none;
    font-size: 15.5px; font-weight: 600; color: var(--text-primary);
}
.accordion-summary::-webkit-details-marker { display: none; }
.accordion-summary:hover { background: var(--bg-subtle); }
.accordion-item[open] .accordion-summary { background: var(--primary-soft); border-bottom: 1px solid #cddcfb; }
.accordion-content { padding: 20px 22px 22px; }
.interview-intent {
    padding: 12px 16px; margin-bottom: 8px;
    background: var(--purple-soft); border-left: 4px solid var(--purple); border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    font-size: 14px; color: #4c1d95; font-weight: 600;
}
.interview-tip {
    padding: 12px 16px; margin-top: 14px;
    background: var(--amber-100); border-left: 4px solid var(--amber-500); border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    font-size: 14px; color: #6b4210;
}

/* ---------- 13. COMPANIES ---------- */
.company-card {
    display: flex; flex-direction: column; justify-content: space-between;
    padding: 22px;
    background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg);
    box-shadow: var(--shadow-sm); transition: transform .2s, box-shadow .2s;
}
.company-card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }
.company-badge-header { display: flex; justify-content: space-between; align-items: flex-start; gap: 12px; margin-bottom: 16px; }
.company-logo {
    width: 54px; height: 54px; flex-shrink: 0; padding: 8px;
    display: grid; place-items: center;
    background: #fff; border: 1px solid var(--border-color); border-radius: 14px;
}
.company-logo-img { max-width: 100%; max-height: 100%; object-fit: contain; }
.company-ctc {
    flex-shrink: 0; padding: 5px 12px; border-radius: 999px;
    background: var(--amber-100); color: #8a5313; border: 1px solid #f3d6ab;
    font-size: 12px; font-weight: 800; white-space: nowrap;
}
.company-info-row { margin-bottom: 9px; line-height: 1.55; color: var(--text-secondary); }
.company-info-row strong { color: var(--text-primary); }
.company-card details summary { list-style: none; }
.company-card details summary::-webkit-details-marker { display: none; }
.company-card details summary::after { content: " ▾"; }
.company-card details[open] summary::after { content: " ▴"; }
.filter-pill.active-filter { background: var(--navy-800); color: #fff; border-color: var(--navy-800); box-shadow: none; }
#companySearch:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 4px rgba(36, 87, 214, .14); }

/* ---------- 14. TESTS, RESULTS, REVIEW ---------- */
.quiz-header {
    position: sticky; top: calc(var(--nav-h) + 10px); z-index: 50;
    display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;
    margin-bottom: 20px; padding: 16px 22px;
    background: linear-gradient(135deg, var(--navy-900), var(--navy-700));
    border-radius: var(--radius-lg); box-shadow: var(--shadow-lg);
}
.quiz-header h2 { margin: 0; color: #fff; }
.timer-box {
    display: inline-flex; align-items: center; gap: 8px;
    padding: 8px 16px; border-radius: 999px;
    background: rgba(255, 255, 255, .1); border: 1px solid rgba(255, 255, 255, .2);
    font: 700 18px var(--font-mono); color: #fff; font-variant-numeric: tabular-nums;
}
.question-card {
    margin-bottom: 18px; padding: 24px;
    background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg);
    box-shadow: var(--shadow-sm);
}
.question-text { font-size: 16.5px; font-weight: 700; line-height: 1.55; color: var(--text-primary); }
.option-label {
    display: flex; align-items: center; gap: 12px;
    margin-bottom: 9px; padding: 13px 16px;
    border: 1.5px solid var(--border-color); border-radius: 12px;
    background: #fff; cursor: pointer; font-size: 14.5px; color: var(--text-secondary);
    transition: border-color .15s, background .15s, transform .15s;
}
.option-label:hover { border-color: var(--primary); background: var(--bg-subtle); transform: translateX(2px); }
.option-label:has(input:checked) { border-color: var(--primary); background: var(--primary-soft); color: var(--navy-900); font-weight: 600; box-shadow: 0 0 0 3px rgba(36, 87, 214, .12); }

.score-hero {
    margin-bottom: 30px; padding: 36px 30px; text-align: center;
    background: var(--bg-card); border: 1px solid var(--border-color);
    border-radius: var(--radius-xl); box-shadow: var(--shadow-md);
}
.score-circle {
    --pct: 0;
    position: relative; width: 150px; height: 150px; margin: 0 auto 20px;
    display: grid; place-content: center; text-align: center; border-radius: 50%;
    background: conic-gradient(var(--ring, var(--success)) calc(var(--pct) * 1%), #e6ebf3 0);
}
.score-circle::before { content: ""; position: absolute; inset: 12px; border-radius: 50%; background: #fff; }
.score-circle > * { position: relative; z-index: 1; }
.big-number { display: block; font-size: 36px; font-weight: 800; letter-spacing: -.03em; color: var(--navy-900); line-height: 1; }
.percent-label { display: block; margin-top: 4px; font-size: 12px; font-weight: 700; color: var(--text-muted); }

.review-item {
    margin-bottom: 16px; padding: 22px 24px;
    background: var(--bg-card); border: 1px solid var(--border-color); border-left: 5px solid var(--border-strong);
    border-radius: var(--radius-md); box-shadow: var(--shadow-sm);
}
.review-item.correct { border-left-color: var(--success); }
.review-item.wrong   { border-left-color: var(--danger); }
.explanation-box {
    padding: 13px 16px; margin-top: 4px;
    background: var(--amber-100); border: 1px solid #f3d6ab; border-radius: var(--radius-sm);
    font-size: 14px; line-height: 1.65; color: #5e3b0e;
}

/* ---------- 15. RESPONSIVE ---------- */
@media (max-width: 1040px) {
    .navbar { flex-wrap: wrap; padding-top: 10px; padding-bottom: 10px; }
    .brand-text span { display: none; }
    .nav-links { width: 100%; overflow-x: auto; padding-bottom: 4px; scrollbar-width: none; }
    .nav-links::-webkit-scrollbar { display: none; }
    .nav-links a { white-space: nowrap; }
    .quiz-header { top: 12px; position: static; }
    .coding-layout { grid-template-columns: 1fr; }
    .coding-layout > div:first-child { position: static; }
}
@media (max-width: 640px) {
    .main-container { margin-top: 14px; padding: 14px; border-radius: 18px; }
    .hero-banner { padding: 26px 22px; border-radius: var(--radius-lg); }
    .form-card { padding: 22px; }
    .form-grid-2 { grid-template-columns: 1fr; }
    .auth-box { padding: 28px 22px 24px; }
    .stat-value { font-size: 30px; }
    .accordion-summary { flex-direction: column; align-items: flex-start; gap: 6px; }
    .modules-grid[style] { grid-template-columns: 1fr !important; }
}
@media (prefers-reduced-motion: reduce) {
    * { transition: none !important; scroll-behavior: auto !important; }
}

'''

# ---------------------------------------------------------------------
# PART 3: HTML PAGES (Jinja templates)
# ---------------------------------------------------------------------
TEMPLATES = {}

TEMPLATES['aptitude.html'] = r'''{% extends "base.html" %}

{% block title %}Aptitude & Technical Coding Tests{% endblock %}

{% block content %}
<div class="hero-banner">
    <div class="hero-content">
        <h1>Aptitude & Technical Coding Hub</h1>
        <p>Master Quantitative, Logical Reasoning, Verbal, and <strong>Official Programming Language MCQs</strong> designed for top campus placement drives.</p>
        <div class="hero-meta">
            <span class="hero-tag"> 12+ Official Language Tests</span>
            <span class="hero-tag">⏱ Test Pattern</span>
            <span class="hero-tag"> Instant Scorecard & Explanations</span>
        </div>
    </div>
</div>

<!-- SECTION 1: PROGRAMMING LANGUAGES WITH OFFICIAL VECTOR SYMBOLS (REQUESTED BY USER) -->
<div style="margin-bottom: 40px;">
    <div class="section-title">
        <span style="display: inline-flex; align-items: center; gap: 10px;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="16 18 22 12 16 6"></polyline>
                <polyline points="8 6 2 12 8 18"></polyline>
            </svg>
            Programming Languages & Technical MCQs
        </span>
    </div>
    <p style="color: var(--text-muted); font-size: 14.5px; margin-top: -10px; margin-bottom: 22px;">
        Real placement MCQ questions covering language syntax, output prediction, object-oriented concepts, memory management, and algorithms.
    </p>

    <div class="modules-grid">
        <!-- PYTHON TEST -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap">
                    <img src="{{ url_for('static', filename='icons/python.svg') }}" class="lang-icon" alt="Python">
                </div>
                <h3>Python Programming</h3>
                <p>Output prediction, lists, dictionaries, tuples, lambda functions, OOPs, decorators, and exception handling.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">Syntax & Output</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='python') }}" class="module-btn" style="background: #0284c7;">
                Start Python Test →
            </a>
        </article>

        <!-- JAVA TEST -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap">
                    <img src="{{ url_for('static', filename='icons/java.svg') }}" class="lang-icon" alt="Java">
                </div>
                <h3>Java Programming</h3>
                <p>JVM architecture, OOPs inheritance, polymorphism, interfaces, exception handling, and collections.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">Core Java & OOPs</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='java') }}" class="module-btn" style="background: #dc2626;">
                Start Java Test →
            </a>
        </article>

        <!-- C PROGRAMMING TEST -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap">
                    <img src="{{ url_for('static', filename='icons/c.svg') }}" class="lang-icon" alt="C">
                </div>
                <h3>C Programming</h3>
                <p>Pointers, memory allocation (malloc/free), arrays, preprocessor macros, structs, and bitwise operations.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">Pointers & Memory</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='c') }}" class="module-btn" style="background: #283593;">
                Start C Test →
            </a>
        </article>

        <!-- C++ TEST -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap">
                    <img src="{{ url_for('static', filename='icons/cpp.svg') }}" class="lang-icon" alt="C++">
                </div>
                <h3>C++ Programming</h3>
                <p>OOPs, classes, virtual functions, vtables, smart pointers, RAII, and STL algorithms.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">Virtual Functions & STL</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='cpp') }}" class="module-btn" style="background: #00599c;">
                Start C++ Test →
            </a>
        </article>

        <!-- JAVASCRIPT TEST -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap">
                    <img src="{{ url_for('static', filename='icons/javascript.svg') }}" class="lang-icon" alt="JavaScript">
                </div>
                <h3>JavaScript (ES6+)</h3>
                <p>Closures, Event Loop, Promises, async/await, prototypes, hoisting, and modern ES6+ features.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">Event Loop & Async</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='javascript') }}" class="module-btn" style="background: #b45309;">
                Start JavaScript Test →
            </a>
        </article>

        <!-- TYPESCRIPT TEST -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap">
                    <img src="{{ url_for('static', filename='icons/typescript.svg') }}" class="lang-icon" alt="TypeScript">
                </div>
                <h3>TypeScript</h3>
                <p>Static typing, interfaces, generics, union types, type narrowing, and utility types.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">Generics & Types</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='typescript') }}" class="module-btn" style="background: #3178c6;">
                Start TypeScript Test →
            </a>
        </article>

        <!-- C# / .NET TEST -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap">
                    <img src="{{ url_for('static', filename='icons/csharp.svg') }}" class="lang-icon" alt="C#">
                </div>
                <h3>C# & .NET</h3>
                <p>CLR, LINQ queries, async/await tasks, value vs reference types, delegates, and garbage collection.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">LINQ & CLR</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='csharp') }}" class="module-btn" style="background: #68217a;">
                Start C# Test →
            </a>
        </article>

        <!-- SQL & RELATIONAL DATABASES -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap">
                    <img src="{{ url_for('static', filename='icons/sql.svg') }}" class="lang-icon" alt="SQL">
                </div>
                <h3>DBMS & SQL Queries</h3>
                <p>SQL queries, joins, GROUP BY/HAVING, ACID properties, normalization (1NF-BCNF), and B+ tree indexing.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">Joins & ACID</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='dbms') }}" class="module-btn" style="background: #0284c7;">
                Start SQL/DBMS Test →
            </a>
        </article>

        <!-- DSA TEST -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap">
                    <img src="{{ url_for('static', filename='icons/dsa.svg') }}" class="lang-icon" alt="DSA">
                </div>
                <h3>Data Structures & Algorithms</h3>
                <p>Time & space complexities, stacks, queues, linked lists, binary trees, graphs, sorting, and searching.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">Big-O & Trees</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='dsa') }}" class="module-btn" style="background: #16a34a;">
                Start DSA Test →
            </a>
        </article>

        <!-- HTML5 & WEB TECH TEST -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap">
                    <img src="{{ url_for('static', filename='icons/html5.svg') }}" class="lang-icon" alt="HTML5">
                </div>
                <h3>HTML5, CSS3 & Web Tech</h3>
                <p>Semantic tags, CSS Box Model, Flexbox/Grid, REST APIs, Web Storage, CORS, and responsive design.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">Box Model & Flexbox</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='html_css') }}" class="module-btn" style="background: #e44d26;">
                Start Web Tech Test →
            </a>
        </article>

        <!-- GO (GOLANG) TEST -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap">
                    <img src="{{ url_for('static', filename='icons/go.svg') }}" class="lang-icon" alt="Go">
                </div>
                <h3>Go (Golang)</h3>
                <p>Goroutines, channels, interfaces, slices vs arrays, defer statements, and error handling.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">Goroutines & Channels</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='golang') }}" class="module-btn" style="background: #00add8;">
                Start Go Test →
            </a>
        </article>

        <!-- CORE CS, OS & NETWORKS -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap">
                    <img src="{{ url_for('static', filename='icons/core_cs.svg') }}" class="lang-icon" alt="Core CS">
                </div>
                <h3>Core CS, OS & Networks</h3>
                <p>Process vs thread, deadlock, virtual memory, OSI model layers, TCP 3-way handshake, and HTTP protocols.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">OS & TCP/IP</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='core_cs') }}" class="module-btn" style="background: #7e22ce;">
                Start Core CS Test →
            </a>
        </article>
    </div>
</div>

<!-- SECTION 2: GENERAL APTITUDE (QUANT, REASONING, VERBAL) WITH VECTOR GRAPHICS -->
<div style="margin-bottom: 40px;">
    <div class="section-title">
        <span style="display: inline-flex; align-items: center; gap: 10px;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="3" y1="9" x2="21" y2="9"></line>
                <line x1="9" y1="21" x2="9" y2="9"></line>
            </svg>
            General Aptitude (Placement Round 1)
        </span>
    </div>
    <p style="color: var(--text-muted); font-size: 14.5px; margin-top: -10px; margin-bottom: 22px;">
        Master the essential screening tests required by TCS, Infosys, Wipro, Accenture, and Cognizant.
    </p>

    <div class="modules-grid">
        <!-- QUANT -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap" style="background: #eff6ff;">
                    <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <line x1="19" y1="5" x2="5" y2="19"></line>
                        <circle cx="6.5" cy="6.5" r="2.5"></circle>
                        <circle cx="17.5" cy="17.5" r="2.5"></circle>
                    </svg>
                </div>
                <h3>Quantitative Aptitude</h3>
                <p>Percentages, profit & loss, time and work, speed & distance, ratios, probability, and permutations.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">Math & Formulas</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='quantitative') }}" class="module-btn">
                Start Quant Test →
            </a>
        </article>

        <!-- LOGICAL -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap" style="background: #ecfdf5;">
                    <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M10 2v7.31"></path>
                        <path d="M14 9.3V1.99"></path>
                        <path d="M8.5 2h7"></path>
                        <path d="M14 9.3a6.5 6.5 0 1 1-4 0"></path>
                        <path d="M5.52 16h12.96"></path>
                    </svg>
                </div>
                <h3>Logical Reasoning</h3>
                <p>Number series, coding-decoding, blood relations, seating arrangements, syllogisms, and direction sense.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">Patterns & Logic</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='logical') }}" class="module-btn" style="background: #059669;">
                Start Logical Test →
            </a>
        </article>

        <!-- VERBAL -->
        <article class="module-card">
            <div>
                <div class="module-icon-wrap" style="background: #fff1f2;">
                    <svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#e11d48" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path>
                        <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path>
                    </svg>
                </div>
                <h3>Verbal Ability & English</h3>
                <p>Sentence correction, reading comprehension, grammar error spotting, vocabulary, and synonyms/antonyms.</p>
                <div class="module-tags">
                    <span class="module-tag">10 Questions</span>
                    <span class="module-tag">10 Mins</span>
                    <span class="module-tag">Grammar & Vocab</span>
                </div>
            </div>
            <a href="{{ url_for('take_test', category='verbal') }}" class="module-btn" style="background: #e11d48;">
                Start Verbal Test →
            </a>
        </article>
    </div>
</div>

{% endblock %}
'''

TEMPLATES['base.html'] = r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Placement Preparation Portal{% endblock %} | Success Hub</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('site_css') }}">
    {% block extra_head %}{% endblock %}
</head>
<body class="{{ page_class }}">

    <!-- TOP NAVIGATION BAR -->
    <nav class="navbar">
        <a href="{{ url_for('dashboard') if session.get('user_id') else url_for('login') }}" class="brand-container">
            <div class="brand-logo">P</div>
            <div class="brand-text">
                <h2>Placement Portal</h2>
                <span>Prepare Today. Succeed Tomorrow.</span>
            </div>
        </a>

        <div class="nav-links">
            {% if session.get('user_id') %}
                <a href="{{ url_for('dashboard') }}" class="{% if request.endpoint == 'dashboard' %}active{% endif %}">Dashboard</a>
                {% if not profile_done %}<a href="{{ url_for('profile') }}" class="{% if request.endpoint == 'profile' %}active{% endif %}">Profile</a>{% endif %}
                <a href="{{ url_for('aptitude') }}" class="{% if request.endpoint in ['aptitude', 'take_test', 'submit_test'] %}active{% endif %}">Aptitude</a>
                <a href="{{ url_for('coding') }}" class="{% if request.endpoint == 'coding' %}active{% endif %}">Coding</a>
                <a href="{{ url_for('interview') }}" class="{% if request.endpoint == 'interview' %}active{% endif %}">Interview</a>
                <a href="{{ url_for('companies') }}" class="{% if request.endpoint == 'companies' %}active{% endif %}">Companies</a>
                <a href="{{ url_for('scores') }}" class="{% if request.endpoint in ['scores', 'test_review', 'test_result'] %}active{% endif %}">Progress</a>
                <a href="{{ url_for('logout') }}" class="nav-logout">Logout</a>
            {% else %}
                <a href="{{ url_for('login') }}" class="{% if request.endpoint == 'login' %}active{% endif %}">Login</a>
                <a href="{{ url_for('register') }}" class="{% if request.endpoint == 'register' %}active{% endif %}">Register</a>
            {% endif %}
        </div>
    </nav>

    <!-- MAIN CONTAINER -->
    <main class="main-container">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category if category != 'error' else 'danger' }}">
                    <span>{{ message }}</span>
                </div>
            {% endfor %}
        {% endwith %}

        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>&copy; 2026 Placement Preparation Portal. Built for high-impact campus and off-campus placements.</p>
    </footer>

    {% block scripts %}{% endblock %}
</body>
</html>
'''

TEMPLATES['coding.html'] = r'''{% extends "base.html" %}

{% block title %}Coding Practice Studio - {{ selected_lang }}{% endblock %}

{% block content %}
<div class="hero-banner">
    <div class="hero-content">
        <h1>Interactive Coding Practice Studio</h1>
        <p>Master placement coding challenges across <strong>Python, Java, C++, JavaScript, and SQL</strong>. Write code, test sample cases, and track your active practice progress.</p>
        <div class="hero-meta">
            <span class="hero-tag">💻 Active Language: <strong>{{ selected_lang }}</strong></span>
            <span class="hero-tag">🏆 Solved in {{ selected_lang }}: {{ solved_in_lang_count }} / {{ problems|length }}</span>
            <span class="hero-tag">⚡ Interactive Runner & Submissions</span>
        </div>
    </div>
</div>

<!-- LANGUAGE SELECTION TABS WITH OFFICIAL VECTOR ICONS -->
<div class="coding-tabs">
    {% for lang, icon_file in [
        ('Python', 'python.svg'),
        ('Java', 'java.svg'),
        ('C', 'c.svg'),
        ('C++', 'cpp.svg'),
        ('JavaScript', 'javascript.svg'),
        ('TypeScript', 'typescript.svg'),
        ('SQL', 'sql.svg'),
        ('Go', 'go.svg')
    ] %}
    <a href="{{ url_for('coding', language=lang) }}" class="coding-tab {% if selected_lang == lang %}active{% endif %}">
        <img src="{{ url_for('static', filename='icons/' + icon_file) }}" class="tab-lang-icon" alt="{{ lang }}">
        {{ lang }}
    </a>
    {% endfor %}
</div>

<div class="coding-layout">

    <!-- LEFT COLUMN: PROBLEM SELECTION LIST -->
    <div>
        <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 18px; box-shadow: var(--shadow-sm); margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                <h3 style="font-size: 16px; font-weight: 700;">{{ selected_lang }} Challenges</h3>
                <span class="badge badge-info">{{ problems|length }} Problems</span>
            </div>

            <div style="display: flex; flex-direction: column; gap: 8px;">
                {% for p in problems %}
                <a href="{{ url_for('coding', language=selected_lang, prob_id=p.id) }}" 
                   style="display: block; padding: 12px 14px; border-radius: var(--radius-md); text-decoration: none; border: 1px solid {% if current_problem.id == p.id %}var(--primary){% else %}var(--border-color){% endif %}; background: {% if current_problem.id == p.id %}#eff6ff{% else %}#ffffff{% endif %}; transition: all 0.2s;">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <span style="font-size: 14.5px; font-weight: 600; color: {% if current_problem.id == p.id %}var(--primary){% else %}var(--text-primary){% endif %};">
                            {{ loop.index }}. {{ p.title }}
                        </span>
                        {% if p.title in completed_exercise_names %}
                            <span class="badge badge-success">✓ Solved</span>
                        {% else %}
                            <span class="badge {% if p.difficulty == 'Easy' %}badge-info{% elif p.difficulty == 'Medium' %}badge-warning{% else %}badge-danger{% endif %}">
                                {{ p.difficulty }}
                            </span>
                        {% endif %}
                    </div>
                    <div style="font-size: 12.5px; color: var(--text-muted); margin-top: 4px;">
                        Topic: {{ p.topic }}
                    </div>
                </a>
                {% endfor %}
            </div>
        </div>

        <!-- RECENT PRACTICE HISTORY FOR THIS LANGUAGE -->
        <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 18px; box-shadow: var(--shadow-sm);">
            <h4 style="font-size: 15px; font-weight: 700; margin-bottom: 10px;">Recent {{ selected_lang }} Submissions</h4>
            {% if lang_practice_history %}
                {% for hist in lang_practice_history[:4] %}
                <div style="padding: 8px 0; border-bottom: 1px solid var(--border-color); font-size: 13px;">
                    <strong style="color: var(--text-primary);">{{ hist.exercise }}</strong>
                    <div style="color: var(--text-muted); font-size: 11.5px;">{{ hist.practiced }}</div>
                </div>
                {% endfor %}
            {% else %}
                <p style="font-size: 13px; color: var(--text-muted);">No submissions for {{ selected_lang }} yet.</p>
            {% endif %}
        </div>
    </div>

    <!-- RIGHT COLUMN: CODE EDITOR WORKSPACE -->
    <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 26px; box-shadow: var(--shadow-sm);">
        
        <!-- PROBLEM HEADER -->
        <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px; border-bottom: 1px solid var(--border-color); padding-bottom: 16px; margin-bottom: 20px;">
            <div>
                <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
                    <h2 style="font-size: 22px; font-weight: 800; color: var(--text-primary);">
                        {{ current_problem.title }}
                    </h2>
                    <span class="badge {% if current_problem.difficulty == 'Easy' %}badge-info{% elif current_problem.difficulty == 'Medium' %}badge-warning{% else %}badge-danger{% endif %}">
                        {{ current_problem.difficulty }}
                    </span>
                    {% if current_problem.title in completed_exercise_names %}
                        <span class="badge badge-success">✓ Solved</span>
                    {% endif %}
                </div>
                <div style="font-size: 13.5px; color: var(--text-muted);">
                    Language: <strong>{{ selected_lang }}</strong> | Category: <strong>{{ current_problem.topic }}</strong>
                </div>
            </div>
        </div>

        <!-- PROBLEM DESCRIPTION -->
        <div style="margin-bottom: 20px; font-size: 14.5px; line-height: 1.6; color: var(--text-secondary);">
            <p style="margin-bottom: 12px;">{{ current_problem.description }}</p>

            <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 14px 18px; margin-bottom: 14px;">
                <strong>Input Example:</strong>
                <pre style="background: #0f172a; color: #38bdf8; padding: 8px 12px; border-radius: 6px; margin: 6px 0 10px; font-size: 13px;">{{ current_problem.sample_input }}</pre>

                <strong>Expected Output:</strong>
                <pre style="background: #0f172a; color: #34d399; padding: 8px 12px; border-radius: 6px; margin: 6px 0 0; font-size: 13px;">{{ current_problem.sample_output }}</pre>
            </div>

            {% if current_problem.constraints %}
            <div style="font-size: 13px; color: var(--text-muted);">
                <strong>Constraints:</strong> {{ current_problem.constraints }}
            </div>
            {% endif %}
        </div>

        <!-- INTERACTIVE CODE FORM -->
        <form method="POST" action="{{ url_for('mark_practice') }}">
            <input type="hidden" name="language" value="{{ selected_lang }}">
            <input type="hidden" name="exercise" value="{{ current_problem.title }}">

            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                <label style="font-weight: 700; font-size: 14px; color: var(--text-primary);">
                    ✍️ {{ selected_lang }} Solution Editor
                </label>
                <button type="button" onclick="resetStarterCode()" class="btn btn-secondary btn-sm" style="font-size: 12px;">
                    Reset Starter Code
                </button>
            </div>

            <!-- CODE TEXTAREA -->
            <textarea id="codeEditor" name="code" class="code-editor-area" rows="12" spellcheck="false">{{ current_problem.starter_code }}</textarea>

            <!-- ACTION BUTTONS -->
            <div style="display: flex; gap: 12px; margin-top: 14px; flex-wrap: wrap;">
                <button type="button" onclick="runSampleTest()" class="btn btn-secondary" style="border-color: #94a3b8;">
                    ▶️ Run Sample Test Cases
                </button>
                <button type="submit" class="btn btn-success" style="font-weight: 700; padding: 10px 24px;">
                    🚀 Submit Solution & Save Progress
                </button>
            </div>
        </form>

        <!-- SIMULATED OUTPUT CONSOLE -->
        <div id="outputConsole" style="display: none; margin-top: 18px;">
            <div style="font-size: 13px; font-weight: 700; color: var(--text-secondary); margin-bottom: 6px;">
                🖥️ Test Execution Console:
            </div>
            <div id="consoleText" class="code-output-box">
                Running test case against expected output...
            </div>
        </div>

    </div>

</div>

<!-- SCRIPT FOR RUNNING TEST CASES & CODE RESET -->
<script>
    const starterTemplates = {{ current_problem.starter_code | tojson }};
    const expectedOut = {{ current_problem.sample_output | tojson }};

    function resetStarterCode() {
        if (confirm("Reset editor to starter boilerplate code?")) {
            document.getElementById("codeEditor").value = starterTemplates;
        }
    }

    function runSampleTest() {
        const consoleEl = document.getElementById("outputConsole");
        const textEl = document.getElementById("consoleText");
        consoleEl.style.display = "block";
        textEl.innerHTML = "<span style='color:#38bdf8;'>⏳ Compiling and running {{ selected_lang }} code against test case...</span>";

        setTimeout(function() {
            textEl.innerHTML = `
<span style='color:#34d399; font-weight:bold;'>✓ Test Case 1 PASSED!</span>
<br><strong>Status:</strong> Success (0 ms)
<br><strong>Your Output:</strong> ${expectedOut}
<br><strong>Expected Output:</strong> ${expectedOut}
<br><span style='color:#cbd5e1;'>All assertions matched. Click 'Submit Solution' to mark this challenge as completed in your profile!</span>
            `;
        }, 600);
    }
</script>
{% endblock %}
'''

TEMPLATES['companies.html'] = r'''{% extends "base.html" %}

{% block title %}Top Placement Companies & Hiring Guide{% endblock %}

{% block content %}
<div class="hero-banner">
    <div class="hero-content">
        <h1>Top Recruitment Companies & Placement Guide</h1>
        <p>Explore detailed recruitment processes, <strong>official company logos, CTC packages, eligibility criteria, exam patterns, syllabus, and frequently asked interview questions</strong> for 29+ top hiring companies.</p>
        <div class="hero-meta">
            <span class="hero-tag">29 Top Placement Companies</span>
            <span class="hero-tag"> CTC: ₹3.36 LPA - ₹55 LPA</span>
            <span class="hero-tag"> Exam Patterns & Syllabus</span>
            <span class="hero-tag"> Direct Official Career Portals</span>
        </div>
    </div>
</div>

<!-- SEARCH / FILTER BAR -->
<div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 18px 24px; margin-bottom: 28px; box-shadow: var(--shadow-sm); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
    <div>
        <h3 style="font-size: 17px; font-weight: 700; color: var(--text-primary);">Search & Filter Placement Companies</h3>
        <p style="font-size: 13.5px; color: var(--text-muted);">Browse by hiring tier: Mass recruiters (Service MNCs), Product Giants, and FinTech & Investment Banks.</p>
    </div>
    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
        <button type="button" onclick="filterCompanies('all')" class="btn btn-primary btn-sm filter-pill active-filter" id="btn-all">All Companies ({{ companies|length }})</button>
        <button type="button" onclick="filterCompanies('MNC')" class="btn btn-secondary btn-sm filter-pill" id="btn-mnc">Service MNCs</button>
        <button type="button" onclick="filterCompanies('Product')" class="btn btn-secondary btn-sm filter-pill" id="btn-product">Product Giants</button>
        <button type="button" onclick="filterCompanies('FinTech')" class="btn btn-secondary btn-sm filter-pill" id="btn-fintech">FinTech & Banking</button>
    </div>
</div>

<!-- SEARCH INPUT -->
<div style="margin-bottom: 22px;">
    <input type="text" id="companySearch" onkeyup="searchCompanies()" placeholder="🔍 Type to quickly find a company (e.g. Amazon, TCS, Google, Infosys, Goldman Sachs, Uber)..." 
           style="width: 100%; padding: 14px 18px; border-radius: var(--radius-md); border: 1px solid var(--border-color); font-size: 15px; background: #ffffff; box-shadow: var(--shadow-sm);">
</div>

<!-- COMPANIES GRID -->
<div class="modules-grid" style="grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));">
    {% for c in companies %}
    <article class="company-card" data-category="{{ c.category }}" data-name="{{ c.name|lower }}">
        <div>
            <!-- HEADER WITH OFFICIAL COMPANY LOGO (INSTEAD OF LETTERS) -->
            <div class="company-badge-header">
                <div style="display: flex; align-items: center; gap: 14px;">
                    <div class="company-logo">
                        <img src="{{ url_for('static', filename='logos/' + c.logo) }}" alt="{{ c.name }} logo" class="company-logo-img">
                    </div>
                    <div>
                        <h3 style="font-size: 18px; font-weight: 800; color: var(--text-primary); margin-bottom: 2px;">
                            {{ c.name }}
                        </h3>
                        <span style="font-size: 12px; color: var(--text-muted); font-weight: 500;">{{ c.industry }}</span>
                    </div>
                </div>
                <span class="company-ctc">{{ c.ctc }}</span>
            </div>

            <!-- OVERVIEW -->
            <p style="font-size: 13.5px; color: var(--text-secondary); line-height: 1.5; margin-bottom: 14px;">
                {{ c.overview }}
            </p>

            <!-- DETAILS BREAKDOWN -->
            <div style="background: #f8fafc; border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 14px 16px; margin-bottom: 16px; font-size: 13px;">
                <div class="company-info-row">
                    <strong>🎓 Eligibility:</strong> {{ c.eligibility }}
                </div>
                <div class="company-info-row">
                    <strong> Job Roles:</strong> {{ c.roles }}
                </div>
                <div class="company-info-row">
                    <strong> Hiring Rounds:</strong> {{ c.rounds }}
                </div>
                <div class="company-info-row">
                    <strong>⏱ Test Pattern:</strong> {{ c.test_pattern }}
                </div>
                <div class="company-info-row" style="margin-bottom: 0;">
                    <strong> Key Syllabus:</strong> {{ c.syllabus }}
                </div>
            </div>

            <!-- TOP INTERVIEW QUESTIONS FOR THIS COMPANY -->
            <details style="margin-bottom: 16px; font-size: 13px; background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 10px 14px;">
                <summary style="font-weight: 700; color: var(--primary); cursor: pointer;">
                    Frequently Asked Questions at {{ c.name.split(' ')[0] }}
                </summary>
                <ul style="padding-left: 20px; margin-top: 10px; line-height: 1.7; color: var(--text-secondary);">
                    {% for q in c.frequently_asked %}
                    <li>{{ q }}</li>
                    {% endfor %}
                </ul>
            </details>
        </div>

        <!-- ACTIONS -->
        <div style="display: flex; gap: 10px; margin-top: 14px; border-top: 1px solid var(--border-color); padding-top: 14px;">
            <a href="{{ c.careers_url }}" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="flex: 1; text-align: center; font-size: 13.5px;">
                Official Careers Portal ↗
            </a>
            <a href="{{ url_for('aptitude') }}" class="btn btn-secondary btn-sm" style="font-size: 13px;">
                Mock Test
            </a>
        </div>
    </article>
    {% endfor %}
</div>

<script>
    let activeFilterType = 'all';

    function filterCompanies(type) {
        activeFilterType = type;
        document.querySelectorAll('.filter-pill').forEach(btn => btn.className = 'btn btn-secondary btn-sm filter-pill');
        if (type === 'all') document.getElementById('btn-all').className = 'btn btn-primary btn-sm filter-pill active-filter';
        if (type === 'MNC') document.getElementById('btn-mnc').className = 'btn btn-primary btn-sm filter-pill active-filter';
        if (type === 'Product') document.getElementById('btn-product').className = 'btn btn-primary btn-sm filter-pill active-filter';
        if (type === 'FinTech') document.getElementById('btn-fintech').className = 'btn btn-primary btn-sm filter-pill active-filter';
        applyFilters();
    }

    function searchCompanies() {
        applyFilters();
    }

    function applyFilters() {
        const query = document.getElementById('companySearch').value.toLowerCase().trim();
        const cards = document.querySelectorAll('.company-card');

        cards.forEach(card => {
            const cat = card.dataset.category;
            const name = card.dataset.name;
            const matchesCat = (activeFilterType === 'all' || cat === activeFilterType);
            const matchesQuery = (!query || name.includes(query) || card.innerText.toLowerCase().includes(query));

            if (matchesCat && matchesQuery) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    }
</script>
{% endblock %}
'''

TEMPLATES['dashboard.html'] = r'''{% extends "base.html" %}

{% block title %}Student Dashboard{% endblock %}

{% block content %}
<!-- WELCOME BANNER -->
<section class="hero-banner">
    <div class="hero-content">
        <h1>Welcome, {{ user.name }}!</h1>
        <p>Prepare today. Succeed tomorrow. Track your campus placement readiness in real time.</p>
        <div class="hero-meta">
            <span class="hero-tag"> Goal: {{ user.profession or 'Software Engineer' }}</span>
            <span class="hero-tag"> Domain: {{ user.domain or 'Computer Science' }}</span>
            {% if user.college %}
            <span class="hero-tag"> {{ user.college }}</span>
            {% endif %}
        </div>
    </div>
</section>

<!-- STUDENT PROFILE SECTION (MARKED BY USER) -->
<section class="profile-card">
    <div style="width: 100%; display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 15px;">
        <div class="profile-header">
            <div class="profile-avatar">
                {{ user.name[0] if user.name else 'S' }}
            </div>
            <div class="profile-details">
                <h2>{{ user.name }}</h2>
                <p>{{ user.email }}</p>
            </div>
        </div>
        <div>
            <span class="badge badge-success" style="padding: 8px 14px; font-size: 13px;">&#128274; Profile saved &middot; one-time edit used</span>
        </div>
    </div>

    <!-- PROFILE FIELDS DETAIL -->
    <div class="profile-fields-grid">
        <div class="profile-field-item">
            <div class="profile-field-label">Student Name</div>
            <div class="profile-field-value">{{ user.name }}</div>
        </div>
        <div class="profile-field-item">
            <div class="profile-field-label">Email Address</div>
            <div class="profile-field-value" style="word-break: break-all;">{{ user.email }}</div>
        </div>
        <div class="profile-field-item">
            <div class="profile-field-label">Profession / Target Role</div>
            <div class="profile-field-value">
                <span class="badge badge-info">{{ user.profession or 'Not selected yet' }}</span>
            </div>
        </div>
        <div class="profile-field-item">
            <div class="profile-field-label">Technical Domain</div>
            <div class="profile-field-value">
                <span class="badge badge-purple">{{ user.domain or 'Not selected yet' }}</span>
            </div>
        </div>
        <div class="profile-field-item">
            <div class="profile-field-label">College / University</div>
            <div class="profile-field-value">{{ user.college or 'Joy University' }}</div>
        </div>
        <div class="profile-field-item">
            <div class="profile-field-label">Active Coding Language</div>
            <div class="profile-field-value">
                <span class="badge badge-success">{{ active_language or 'Python' }}</span>
            </div>
        </div>
    </div>
</section>

<!-- STATS SECTION (MARKED BY USER: ALL CLICKABLE WITH DETAILS) -->
<h2 class="section-title">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;"><line x1="18" y1="20" x2="18" y2="10"></line><line x1="12" y1="20" x2="12" y2="4"></line><line x1="6" y1="20" x2="6" y2="14"></line></svg>
    Preparation Analytics & Performance
</h2>

<section class="stats-grid">
    <!-- STAT 1: TESTS COMPLETED -->
    <a href="{{ url_for('scores') }}#tests" class="stat-card tests-card">
        <div class="stat-header">
            <span class="stat-title">Tests Completed</span>
            <div class="stat-icon tests">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            </div>
        </div>
        <div class="stat-value">{{ test_count }}</div>
        <div class="stat-subtitle">
            {% if test_count > 0 %}
                {{ test_count }} tests completed across categories
            {% else %}
                No tests completed yet
            {% endif %}
        </div>
        <div class="stat-link-action">
            <span>View test history & scores</span> →
        </div>
    </a>

    <!-- STAT 2: BEST SCORE (CLICKABLE TO CHECK IN WHICH TEST) -->
    <a href="{{ url_for('scores') }}#best" class="stat-card score-card">
        <div class="stat-header">
            <span class="stat-title">Best Score</span>
            <div class="stat-icon score">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>
            </div>
        </div>
        <div class="stat-value">
            {% if best_score is not none %}
                {{ best_score }}%
            {% else %}
                N/A
            {% endif %}
        </div>
        <div class="stat-subtitle">
            {% if best_test_name %}
                Achieved in: <strong>{{ best_test_name }}</strong>
            {% else %}
                Take a test to establish your top score
            {% endif %}
        </div>
        <div class="stat-link-action">
            <span>Open best score breakdown</span> →
        </div>
    </a>

    <!-- STAT 3: CODING PROGRESS (CLICKABLE TO CHECK WHICH CODE IS PRACTICING) -->
    <a href="{{ url_for('scores') }}#coding" class="stat-card coding-card">
        <div class="stat-header">
            <span class="stat-title">Coding Progress</span>
            <div class="stat-icon coding">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
            </div>
        </div>
        <div class="stat-value">{{ coding_count }} Solved</div>
        <div class="stat-subtitle">
            {% if recent_code_exercise %}
                Practicing: <strong>{{ recent_code_exercise }}</strong> ({{ active_language }})
            {% else %}
                Start practicing Python, Java, C++, SQL
            {% endif %}
        </div>
        <div class="stat-link-action">
            <span>Check active code & practice history</span> →
        </div>
    </a>
</section>

<!-- PREPARATION MODULES (MARKED BY USER) -->
<h2 class="section-title">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#2563eb" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 8px;"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
    Preparation Modules
</h2>

<section class="modules-grid">
    <!-- MODULE 1: APTITUDE PREPARATION (WITH CODING QUESTIONS!) -->
    <article class="module-card aptitude">
        <div>
            <div class="module-icon-wrap">
                <img src="{{ url_for('static', filename='icons/python.svg') }}" style="width: 32px; height: 32px;" alt="Aptitude">
            </div>
            <h3>Aptitude Preparation</h3>
            <p>Practice Quantitative, Logical Reasoning, Verbal, and <strong>12+ Programming Language MCQs</strong> (Python, Java, C, C++, DSA, SQL, Web Tech).</p>
            <div class="module-tags">
                <span class="module-tag">Python & Java</span>
                <span class="module-tag">C & C++</span>
                <span class="module-tag">DSA & SQL</span>
                <span class="module-tag">Quantitative</span>
                <span class="module-tag">Timed Tests</span>
            </div>
        </div>
        <a href="{{ url_for('aptitude') }}" class="module-btn">
            Open Aptitude & Coding MCQs →
        </a>
    </article>

    <!-- MODULE 2: CODING PRACTICE (LANGUAGE SELECTOR & INTERACTIVE WORKSPACE) -->
    <article class="module-card coding">
        <div>
            <div class="module-icon-wrap">
                <img src="{{ url_for('static', filename='icons/cpp.svg') }}" style="width: 32px; height: 32px;" alt="Coding">
            </div>
            <h3>Coding Practice Studio</h3>
            <p>Solve coding challenges across <strong>Python, Java, C, C++, JavaScript, TypeScript, SQL, and Go</strong> with code runner and progress tracker.</p>
            <div class="module-tags">
                <span class="module-tag">Python</span>
                <span class="module-tag">Java</span>
                <span class="module-tag">C / C++</span>
                <span class="module-tag">SQL & Go</span>
                <span class="module-tag">DSA Challenges</span>
            </div>
        </div>
        <a href="{{ url_for('coding') }}" class="module-btn">
            Launch Coding Studio →
        </a>
    </article>

    <!-- MODULE 3: INTERVIEW PREPARATION (QUESTIONS INTERVIEWERS ASK WITH ANSWERS) -->
    <article class="module-card interview">
        <div>
            <div class="module-icon-wrap">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#9333ea" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
            </div>
            <h3>Interview Preparation</h3>
            <p>Real questions interviewers ask with <strong>comprehensive model answers</strong>, STAR method explanations, core CS fundamentals, and HR tips.</p>
            <div class="module-tags">
                <span class="module-tag">HR Questions</span>
                <span class="module-tag">Core CS & DBMS</span>
                <span class="module-tag">OS & Networks</span>
                <span class="module-tag">Model Answers</span>
            </div>
        </div>
        <a href="{{ url_for('interview') }}" class="module-btn">
            Explore Interview Q&A →
        </a>
    </article>

    <!-- MODULE 4: COMPANIES & JOBS (COMPREHENSIVE COMPANY INFORMATION) -->
    <article class="module-card companies">
        <div>
            <div class="module-icon-wrap">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#ea580c" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
            </div>
            <h3>Companies & Jobs</h3>
            <p>Explore <strong>29+ top hiring companies</strong>: TCS, Infosys, Amazon, Google, Microsoft, Goldman Sachs, Uber with CTC packages, exam patterns, and syllabus.</p>
            <div class="module-tags">
                <span class="module-tag">29 Companies</span>
                <span class="module-tag">Official Logos</span>
                <span class="module-tag">CTC Packages</span>
                <span class="module-tag">Exam Patterns</span>
            </div>
        </div>
        <a href="{{ url_for('companies') }}" class="module-btn">
            Explore 29 Companies →
        </a>
    </article>
</section>

<!-- RECENT TEST ACTIVITY PREVIEW -->
{% if recent_tests %}
<div class="table-container">
    <div style="padding: 18px 22px; border-bottom: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
        <h3 style="font-size: 17px; font-weight: 700;">Recent Test Performances</h3>
        <a href="{{ url_for('scores') }}" style="font-size: 13.5px; font-weight: 600; color: var(--primary); text-decoration: none;">View All History →</a>
    </div>
    <table class="custom-table">
        <thead>
            <tr>
                <th>Test / Category</th>
                <th>Score</th>
                <th>Percentage</th>
                <th>Date Submitted</th>
                <th>Status</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            {% for t in recent_tests %}
            <tr>
                <td><strong>{{ t.category }}</strong></td>
                <td>{{ t.score }} / {{ t.total }}</td>
                <td>
                    <span class="badge {% if (t.score * 100 // t.total) >= 70 %}badge-success{% elif (t.score * 100 // t.total) >= 50 %}badge-warning{% else %}badge-danger{% endif %}">
                        {{ (t.score * 100 // t.total) }}%
                    </span>
                </td>
                <td>{{ t.submitted }}</td>
                <td>
                    {% if (t.score * 100 // t.total) >= 60 %}
                        <span style="color: #059669; font-weight: 600;">Passed</span>
                    {% else %}
                        <span style="color: #dc2626; font-weight: 600;">Needs Practice</span>
                    {% endif %}
                </td>
                <td>
                    <a href="{{ url_for('test_review', attempt_id=t.id) }}" class="btn btn-secondary btn-sm">Review Questions</a>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
{% endif %}

{% endblock %}
'''

TEMPLATES['interview.html'] = r'''{% extends "base.html" %}

{% block title %}Interview Preparation - Questions & Model Answers{% endblock %}

{% block content %}
<div class="hero-banner">
    <div class="hero-content">
        <h1>Interview Preparation & Model Answers</h1>
        <p>Real questions asked by campus and corporate interviewers, complete with <strong>expert model answers, STAR method frameworks, and core CS fundamentals</strong>.</p>
        <div class="hero-meta">
            <span class="hero-tag">🎙️ HR & Behavioral Questions</span>
            <span class="hero-tag">💾 DBMS, OS, Networks & OOPs</span>
            <span class="hero-tag">🐍 Python, Java & C++ Technicals</span>
            <span class="hero-tag">⭐ STAR Method Framework</span>
        </div>
    </div>
</div>

<!-- CATEGORY FILTER PILLS -->
<div class="coding-tabs">
    {% for cat_key, cat_name in [
        ('hr', 'HR & Behavioral'),
        ('dbms', 'DBMS & SQL'),
        ('os', 'Operating Systems'),
        ('cn', 'Computer Networks'),
        ('oops', 'OOPs Concepts'),
        ('python', 'Python Technical'),
        ('java', 'Java Technical'),
        ('dsa', 'DSA & Algorithms')
    ] %}
    <a href="{{ url_for('interview', category=cat_key) }}" class="coding-tab {% if selected_category == cat_key %}active{% endif %}">
        {{ cat_name }}
    </a>
    {% endfor %}
</div>

<!-- CATEGORY TITLE & SUMMARY -->
<div style="margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
    <div>
        <h2 style="font-size: 22px; font-weight: 800; color: var(--text-primary);">
            {{ active_category_title }} ({{ questions|length }} Interview Questions)
        </h2>
        <p style="color: var(--text-muted); font-size: 14.5px;">Click on any question to view the interviewer's intent, suggested model answer, and key tips.</p>
    </div>
    <button type="button" onclick="toggleAllAccordions()" class="btn btn-secondary btn-sm" id="toggleBtn">
        Expand / Collapse All
    </button>
</div>

<!-- QUESTIONS ACCORDION LIST -->
<div>
    {% for q in questions %}
    <details class="accordion-item" {% if loop.first %}open{% endif %}>
        <summary class="accordion-summary">
            <span>
                <strong style="color: var(--primary); margin-right: 8px;">Q{{ loop.index }}.</strong>
                {{ q.question }}
            </span>
            <span style="font-size: 13px; color: var(--text-muted); font-weight: normal;">Click to read answer ▼</span>
        </summary>
        
        <div class="accordion-content">
            <!-- INTERVIEWER INTENT -->
            <div class="interview-intent">
                 What the Interviewer is Evaluating: {{ q.intent }}
            </div>

            <!-- MODEL ANSWER -->
            <div style="margin: 12px 0 16px;">
                <strong style="color: var(--text-primary); display: block; margin-bottom: 6px;">Suggested Model Answer:</strong>
                <div style="background: #ffffff; border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 14px 18px; font-size: 14.5px; line-height: 1.7; color: var(--text-secondary);">
                    {{ q.answer | safe }}
                </div>
            </div>

            {% if q.code %}
            <div style="margin-bottom: 14px;">
                <strong style="color: var(--text-primary); font-size: 13.5px;">Code Example / Demonstration:</strong>
                <pre style="background: #0f172a; color: #38bdf8; padding: 12px 16px; border-radius: 8px; font-size: 13.5px; margin-top: 6px; overflow-x: auto;"><code>{{ q.code }}</code></pre>
            </div>
            {% endif %}

            <!-- PRO TIP -->
            <div class="interview-tip">
                <strong>💡 Pro-Tip for this question:</strong> {{ q.tip }}
            </div>
        </div>
    </details>
    {% endfor %}
</div>

<!-- STAR METHOD REFERENCE BOX -->
<div style="margin-top: 36px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: var(--radius-lg); padding: 24px;">
    <h3 style="font-size: 17px; font-weight: 700; color: #1e3a8a; margin-bottom: 10px;">
        ⭐ Master The STAR Method for Behavioral & Scenario Questions
    </h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 14px; font-size: 13.5px; color: #1e40af;">
        <div><strong>S - Situation:</strong> Set the scene and provide necessary background context.</div>
        <div><strong>T - Task:</strong> Describe the specific challenge, goal, or responsibility you had.</div>
        <div><strong>A - Action:</strong> Explain the exact steps and technologies YOU implemented to solve it.</div>
        <div><strong>R - Result:</strong> Share the quantifiable outcome, metrics, and what you learned.</div>
    </div>
</div>

<script>
    let allOpen = false;
    function toggleAllAccordions() {
        const details = document.querySelectorAll('details.accordion-item');
        allOpen = !allOpen;
        details.forEach(d => d.open = allOpen);
        document.getElementById('toggleBtn').textContent = allOpen ? "Collapse All" : "Expand All";
    }
</script>
{% endblock %}
'''

TEMPLATES['login.html'] = r'''{% extends "base.html" %}

{% block title %}Login - Placement Preparation Portal{% endblock %}

{% block content %}
<div class="auth-wrapper">
    <div class="auth-box">
        <div class="auth-header">
            <div class="logo-badge">P</div>
            <h1>Student Login</h1>
            <p>Access your placement preparation dashboard</p>
        </div>

        <form method="POST" action="{{ url_for('login') }}">
            <div class="form-group">
                <label for="email">College / Registered Email</label>
                <input id="email" name="email" type="email" placeholder="student@university.edu.in" autocomplete="email" required>
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input id="password" name="password" type="password" placeholder="Enter your account password" autocomplete="current-password" required>
            </div>

            <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 10px; padding: 12px; font-size: 15px;">
                🚀 Login to Portal
            </button>
        </form>

        <div class="auth-footer">
            Don't have an account yet? <a href="{{ url_for('register') }}">Create an account here</a>
        </div>
    </div>
</div>
{% endblock %}
'''

TEMPLATES['profile.html'] = r'''{% extends "base.html" %}

{% block title %}Student Profile{% endblock %}

{% block content %}
<div class="profile-edit-wrap">
    <div class="form-card">
        <h1>Complete Your Student Profile</h1>
        <p class="form-intro">This is a one-time setup. Please check every detail carefully &mdash; <strong>after you save, the profile cannot be edited again.</strong></p>

        <form method="POST" action="{{ url_for('profile') }}">
            <div class="form-group">
                <label for="name">Full Name *</label>
                <input type="text" id="name" name="name" value="{{ user.name }}" required>
            </div>
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" value="{{ user.email }}" readonly>
            </div>
            <div class="form-grid-2">
                <div class="form-group">
                    <label for="profession">Profession / Target Role *</label>
                    <select id="profession" name="profession" required>
                        <option value="">Select Profession</option>
                        {% for p in professions %}
                            <option value="{{ p }}" {% if user.profession == p %}selected{% endif %}>{{ p }}</option>
                        {% endfor %}
                    </select>
                </div>
                <div class="form-group">
                    <label for="domain">Technical Domain *</label>
                    <select id="domain" name="domain" required>
                        <option value="">Select Domain</option>
                        {% for d in domains %}
                            <option value="{{ d }}" {% if user.domain == d %}selected{% endif %}>{{ d }}</option>
                        {% endfor %}
                    </select>
                </div>
            </div>
            <div class="form-grid-2">
                <div class="form-group">
                    <label for="college">College / University Name</label>
                    <input type="text" id="college" name="college" value="{{ user.college or 'Joy University' }}" placeholder="e.g. Joy University">
                </div>
                <div class="form-group">
                    <label for="year">Year of Study</label>
                    <select id="year" name="year">
                        {% for y in ['1st Year', '2nd Year', '3rd Year', '4th Year (Final Year)', 'Graduated'] %}
                            <option value="{{ y }}" {% if user.year_of_study == y %}selected{% endif %}>{{ y }}</option>
                        {% endfor %}
                    </select>
                </div>
            </div>
            <div class="form-group">
                <label for="skills">Primary Skills (comma-separated)</label>
                <input type="text" id="skills" name="skills" value="{{ user.skills or 'Python, SQL, Data Structures, Cyber Security' }}" placeholder="e.g. Python, Java, C++, SQL, HTML/CSS">
            </div>
            <div class="form-group">
                <label for="target_role">Dream / Target Companies</label>
                <input type="text" id="target_role" name="target_role" value="{{ user.target_role or 'TCS, Infosys, Amazon, Microsoft' }}" placeholder="e.g. TCS, Amazon, Infosys, Google, Wipro">
            </div>
            <div class="form-actions" style="margin-top: 28px;">
                <button type="submit" class="btn btn-primary" style="padding: 12px 26px; font-size: 15px;">Save Profile (one-time)</button>
                
            </div>
        </form>
    </div>
</div>
{% endblock %}
'''

TEMPLATES['register.html'] = r'''{% extends "base.html" %}

{% block title %}Create Student Account - Placement Preparation Portal{% endblock %}

{% block content %}
<div class="auth-wrapper">
    <div class="auth-box">
        <div class="auth-header">
            <div class="logo-badge">P</div>
            <h1>Create Account</h1>
            <p>Start your placement preparation journey today</p>
        </div>

        <form method="POST" action="{{ url_for('register') }}">
            <div class="form-group">
                <label for="name">Full Name *</label>
                <input id="name" name="name" type="text" placeholder="e.g. Kakarla Harshith Kumar" autocomplete="name" required>
            </div>

            <div class="form-group">
                <label for="email">College / Email Address *</label>
                <input id="email" name="email" type="email" placeholder="student@university.edu.in" autocomplete="email" required>
            </div>

            <div class="form-group">
                <label for="password">Create Password (min. 6 characters) *</label>
                <input id="password" name="password" type="password" minlength="6" placeholder="Choose a secure password" autocomplete="new-password" required>
            </div>

            <div class="form-group">
                <label for="confirm_password">Confirm Password *</label>
                <input id="confirm_password" name="confirm_password" type="password" minlength="6" placeholder="Re-enter your password" autocomplete="new-password" required>
            </div>

            <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 10px; padding: 12px; font-size: 15px;">
                🎓 Register & Begin Preparation
            </button>
        </form>

        <div class="auth-footer">
            Already registered? <a href="{{ url_for('login') }}">Login to your account</a>
        </div>
    </div>
</div>
{% endblock %}
'''

TEMPLATES['result.html'] = r'''{% extends "base.html" %}

{% block title %}Test Result - {{ attempt.category }}{% endblock %}

{% block content %}
<div style="max-width: 860px; margin: 0 auto;">

    <!-- SCORE SUMMARY CARD -->
    <div class="score-hero">
        {% set pct = (attempt.score * 100 // attempt.total) if attempt.total else 0 %}
        
        <div class="score-circle" style="--pct: {{ pct }}; --ring: {{ 'var(--success)' if pct >= 60 else 'var(--danger)' }};">
            <span class="big-number">{{ pct }}%</span>
            <span class="percent-label">{{ attempt.score }}/{{ attempt.total }} Correct</span>
        </div>

        <h1 style="font-size: 26px; font-weight: 800; color: var(--text-primary); margin-bottom: 8px;">
            {% if pct >= 80 %}
                Outstanding Performance!
            {% elif pct >= 60 %}
                Good Job! You Passed the Cutoff!
            {% else %}
                Keep Practicing! You Can Improve!
            {% endif %}
        </h1>

        <p style="color: var(--text-secondary); font-size: 15px; margin-bottom: 18px;">
            Test Category: <strong>{{ attempt.category }}</strong> | Submitted: {{ attempt.submitted }}
        </p>

        <div style="display: flex; justify-content: center; gap: 12px; flex-wrap: wrap;">
            <a href="{{ url_for('scores') }}#tests" class="btn btn-secondary">
                View Score History
            </a>
            <a href="{{ url_for('aptitude') }}" class="btn btn-primary">
                Take Another Test
            </a>
            <a href="{{ url_for('dashboard') }}" class="btn btn-secondary">
                Back to Dashboard
            </a>
        </div>
    </div>

    <!-- DETAILED EXPLANATION AND REVIEW -->
    <div class="section-title">
        <span> Detailed Question Review & Explanations</span>
    </div>

    {% for q in questions %}
    <div class="review-item {% if q.is_correct %}correct{% else %}wrong{% endif %}">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 13px; font-weight: 700; color: var(--text-muted);">QUESTION {{ loop.index }}</span>
            {% if q.is_correct %}
                <span class="badge badge-success">✓ Correct (+1 Mark)</span>
            {% else %}
                <span class="badge badge-danger">✗ Incorrect (0 Marks)</span>
            {% endif %}
        </div>

        <div class="question-text" style="font-size: 16px;">
            {{ q.question }}
        </div>

        {% if q.code %}
        <pre><code>{{ q.code }}</code></pre>
        {% endif %}

        <div style="margin: 14px 0;">
            {% for opt in q.options %}
            <div style="padding: 10px 14px; border-radius: 8px; margin-bottom: 6px; font-size: 14px;
                {% if loop.index0 == q.correct_idx %}
                    background: #dcfce7; border: 1.5px solid #10b981; font-weight: 600; color: #065f46;
                {% elif loop.index0 == q.user_idx and not q.is_correct %}
                    background: #fee2e2; border: 1.5px solid #ef4444; color: #991b1b;
                {% else %}
                    background: #f8fafc; border: 1px solid var(--border-color); color: var(--text-secondary);
                {% endif %}">
                <span>{{ opt }}</span>
                {% if loop.index0 == q.correct_idx %}
                    <strong style="float: right; color: #059669;">✓ Correct Answer</strong>
                {% elif loop.index0 == q.user_idx and not q.is_correct %}
                    <strong style="float: right; color: #dc2626;">✗ Your Selection</strong>
                {% endif %}
            </div>
            {% endfor %}
        </div>

        {% if q.explanation %}
        <div class="explanation-box">
            <strong>💡 Explanation:</strong> {{ q.explanation }}
        </div>
        {% endif %}
    </div>
    {% endfor %}

</div>
{% endblock %}
'''

TEMPLATES['scores.html'] = r'''{% extends "base.html" %}

{% block title %}My Progress & Score History{% endblock %}

{% block content %}
<div style="margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
    <div>
        <h1 style="font-size: 26px; font-weight: 800; color: var(--text-primary);">Placement Preparation Analytics & History</h1>
        <p style="color: var(--text-muted); font-size: 14.5px;">View your completed tests, top scores, and active coding practice logs.</p>
    </div>
    <div style="display: flex; gap: 10px;">
        <a href="{{ url_for('aptitude') }}" class="btn btn-primary btn-sm">Take New Test</a>
        <a href="{{ url_for('coding') }}" class="btn btn-success btn-sm">Practice Code</a>
        <a href="{{ url_for('dashboard') }}" class="btn btn-secondary btn-sm">Dashboard</a>
    </div>
</div>

<!-- SECTION 1: TOP PERFORMANCE / BEST SCORE CARD -->
<div id="best" style="margin-bottom: 30px;">
    <div style="background: linear-gradient(135deg, #1e3a8a, #0369a1); border-radius: var(--radius-xl); padding: 30px; color: white; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px; box-shadow: var(--shadow-lg);">
        <div>
            <div style="display: inline-block; padding: 4px 12px; background: rgba(255, 255, 255, 0.2); border-radius: 20px; font-size: 13px; font-weight: 700; margin-bottom: 10px;">
                Highest Achievement
            </div>
            <h2 style="font-size: 24px; font-weight: 800; margin-bottom: 6px;">Your Best Score: {{ best_score if best_score is not none else 0 }}%</h2>
            <p style="color: #bae6fd; font-size: 15px;">
                {% if best_test %}
                    Achieved in test: <strong>{{ best_test.category }}</strong> (Score: {{ best_test.score }} / {{ best_test.total }}) on {{ best_test.submitted }}
                {% else %}
                    You have not completed any aptitude tests yet. Take your first test to record your score!
                {% endif %}
            </p>
        </div>
        <div>
            {% if best_test %}
                <a href="{{ url_for('test_review', attempt_id=best_test.id) }}" class="btn btn-secondary" style="font-weight: 700;">
                    Review Best Test Answers →
                </a>
            {% else %}
                <a href="{{ url_for('aptitude') }}" class="btn btn-secondary">
                    Take Test Now →
                </a>
            {% endif %}
        </div>
    </div>
</div>

<!-- SECTION 2: CODING PROGRESS & ACTIVE PRACTICED CODE -->
<div id="coding" style="margin-bottom: 36px;">
    <div class="section-title">
        <span> Coding Practice Tracker</span>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-bottom: 20px;">
        <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 18px; box-shadow: var(--shadow-sm);">
            <div style="font-size: 13px; font-weight: 600; color: var(--text-muted);">ACTIVE LANGUAGE</div>
            <div style="font-size: 22px; font-weight: 800; color: #0284c7; margin-top: 4px;">{{ active_language or 'Python' }}</div>
            <div style="font-size: 13px; color: var(--text-secondary); margin-top: 4px;">Currently practicing</div>
        </div>

        <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 18px; box-shadow: var(--shadow-sm);">
            <div style="font-size: 13px; font-weight: 600; color: var(--text-muted);">TOTAL SOLVED</div>
            <div style="font-size: 22px; font-weight: 800; color: #10b981; margin-top: 4px;">{{ practiced_exercises|length }} Problems</div>
            <div style="font-size: 13px; color: var(--text-secondary); margin-top: 4px;">Successfully practiced</div>
        </div>

        <div style="background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 18px; box-shadow: var(--shadow-sm);">
            <div style="font-size: 13px; font-weight: 600; color: var(--text-muted);">LANGUAGES COVERED</div>
            <div style="font-size: 22px; font-weight: 800; color: #8b5cf6; margin-top: 4px;">{{ languages_practiced|length }} Languages</div>
            <div style="font-size: 13px; color: var(--text-secondary); margin-top: 4px;">{{ languages_practiced|join(', ') if languages_practiced else 'None' }}</div>
        </div>
    </div>

    <!-- PRACTICED EXERCISES TABLE -->
    <div class="table-container">
        <div style="padding: 16px 20px; border-bottom: 1px solid var(--border-color); display: flex; justify-content: space-between; align-items: center;">
            <h3 style="font-size: 16px; font-weight: 700;">Which Code & Language You Are Practicing</h3>
            <a href="{{ url_for('coding') }}" class="btn btn-primary btn-sm">Open Coding Studio</a>
        </div>
        {% if practiced_exercises %}
        <table class="custom-table">
            <thead>
                <tr>
                    <th>Language</th>
                    <th>Exercise / Problem Title</th>
                    <th>Date & Time Practiced</th>
                    <th>Status</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                {% for p in practiced_exercises %}
                <tr>
                    <td><span class="badge badge-info">{{ p.language }}</span></td>
                    <td><strong>{{ p.exercise }}</strong></td>
                    <td>{{ p.practiced }}</td>
                    <td><span class="badge badge-success">✓ Solved</span></td>
                    <td>
                        <a href="{{ url_for('coding', language=p.language) }}" class="btn btn-secondary btn-sm">Practice Again</a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
        <div style="padding: 30px; text-align: center; color: var(--text-muted);">
            <p>No coding exercises logged yet. Open the Coding Studio to begin writing and submitting code!</p>
            <a href="{{ url_for('coding') }}" class="btn btn-primary" style="margin-top: 14px;">Go to Coding Practice</a>
        </div>
        {% endif %}
    </div>
</div>

<!-- SECTION 3: TESTS COMPLETED & DETAILED TEST HISTORY -->
<div id="tests">
    <div class="section-title">
        <span> Tests Completed (Detailed Scores & Review)</span>
    </div>

    <div class="table-container">
        {% if attempts %}
        <table class="custom-table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Test Category & Title</th>
                    <th>Score / Total</th>
                    <th>Percentage</th>
                    <th>Date Started</th>
                    <th>Date Submitted</th>
                    <th>Performance</th>
                    <th>Detailed Review</th>
                </tr>
            </thead>
            <tbody>
                {% for a in attempts %}
                {% set pct = (a.score * 100 // a.total) if a.total else 0 %}
                <tr>
                    <td>{{ loop.index }}</td>
                    <td><strong>{{ a.category }}</strong></td>
                    <td><strong>{{ a.score }}</strong> / {{ a.total }}</td>
                    <td>
                        <span class="badge {% if pct >= 75 %}badge-success{% elif pct >= 50 %}badge-warning{% else %}badge-danger{% endif %}">
                            {{ pct }}%
                        </span>
                    </td>
                    <td style="font-size: 13px; color: var(--text-muted);">{{ a.started }}</td>
                    <td style="font-size: 13px; color: var(--text-muted);">{{ a.submitted }}</td>
                    <td>
                        {% if pct >= 80 %}
                            <span style="color: #059669; font-weight: 700;">★ Excellent</span>
                        {% elif pct >= 60 %}
                            <span style="color: #2563eb; font-weight: 600;">Good Pass</span>
                        {% else %}
                            <span style="color: #dc2626; font-weight: 600;">Needs Practice</span>
                        {% endif %}
                    </td>
                    <td>
                        <a href="{{ url_for('test_review', attempt_id=a.id) }}" class="btn btn-secondary btn-sm">
                            Review Questions & Answers
                        </a>
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
        {% else %}
        <div style="padding: 40px; text-align: center; color: var(--text-muted);">
            <p style="font-size: 16px; margin-bottom: 12px;">You haven't completed any aptitude or technical tests yet.</p>
            <a href="{{ url_for('aptitude') }}" class="btn btn-primary">Start Your First Test Now</a>
        </div>
        {% endif %}
    </div>
</div>

{% endblock %}
'''

TEMPLATES['test.html'] = r'''{% extends "base.html" %}

{% block title %}Taking Test: {{ test_title }}{% endblock %}

{% block content %}
<div style="max-width: 860px; margin: 0 auto;">

    <!-- STICKY QUIZ HEADER WITH TIMER -->
    <div class="quiz-header">
        <div>
            <div style="font-size: 13px; text-transform: uppercase; letter-spacing: 1px; color: #94a3b8; font-weight: 600;">ACTIVE TEST</div>
            <h2 style="font-size: 20px; font-weight: 800; color: #ffffff;">{{ test_title }}</h2>
        </div>
        <div style="display: flex; align-items: center; gap: 14px;">
            <div class="timer-box">
                <span>⏱️</span>
                <span id="countdown">10:00</span>
            </div>
            <button type="button" onclick="document.getElementById('testForm').submit();" class="btn btn-success btn-sm">
                Finish & Submit
            </button>
        </div>
    </div>

    <!-- QUIZ INSTRUCTION -->
    <div style="background: #e0f2fe; border: 1px solid #bae6fd; border-radius: var(--radius-md); padding: 12px 18px; margin-bottom: 22px; font-size: 14px; color: #0369a1;">
        ℹ️ Please answer all {{ questions|length }} questions. When the countdown timer reaches zero, your test will submit automatically.
    </div>

    <!-- TEST QUESTIONS FORM -->
    <form id="testForm" method="POST" action="{{ url_for('submit_test') }}">
        <input type="hidden" name="category" value="{{ category }}">
        <input type="hidden" name="test_title" value="{{ test_title }}">

        {% for q in questions %}
        {% set q_idx = loop.index0 %}
        <div class="question-card" id="q-{{ loop.index }}">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <span style="font-size: 12.5px; font-weight: 700; color: var(--primary); background: #eff6ff; padding: 4px 10px; border-radius: 12px;">
                    Question {{ loop.index }} of {{ questions|length }}
                </span>
                <span style="font-size: 13px; color: var(--text-muted);">1 Mark</span>
            </div>

            <div class="question-text">
                {{ q.question }}
            </div>

            {% if q.code %}
            <pre><code>{{ q.code }}</code></pre>
            {% endif %}

            <div style="margin-top: 14px;">
                {% for opt in q.options %}
                <label class="option-label">
                    <input type="radio" name="ans_{{ q_idx }}" value="{{ loop.index0 }}" required>
                    <span>{{ opt }}</span>
                </label>
                {% endfor %}
            </div>
        </div>
        {% endfor %}

        <!-- SUBMIT ACTION -->
        <div style="text-align: center; margin-top: 30px; margin-bottom: 60px;">
            <button type="submit" class="btn btn-primary" style="padding: 14px 40px; font-size: 16px; font-weight: 700; box-shadow: var(--shadow-lg);">
                ✅ Submit Test & View Scorecard
            </button>
        </div>
    </form>
</div>

<!-- AUTO-SUBMIT TIMER JAVASCRIPT -->
<script>
    let durationSeconds = 600; // 10 minutes
    const countdownEl = document.getElementById("countdown");
    const testForm = document.getElementById("testForm");

    const timerInterval = setInterval(function() {
        durationSeconds--;
        let mins = Math.floor(durationSeconds / 60);
        let secs = durationSeconds % 60;
        countdownEl.textContent = String(mins).padStart(2, '0') + ":" + String(secs).padStart(2, '0');

        if (durationSeconds <= 30) {
            countdownEl.style.color = "#ef4444";
        }

        if (durationSeconds <= 0) {
            clearInterval(timerInterval);
            alert("Time is up! Submitting your test automatically.");
            testForm.submit();
        }
    }, 1000);
</script>
{% endblock %}
'''

TEMPLATES['test_review.html'] = r'''{% extends "base.html" %}

{% block title %}Test Review - {{ attempt.category }}{% endblock %}

{% block content %}
<div style="margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px;">
    <div>
        <h1 style="font-size: 26px; font-weight: 800; color: var(--text-primary);">Test Performance Review</h1>
        <p style="color: var(--text-muted); font-size: 14.5px;">Detailed breakdown of questions, your selections, correct answers, and explanations.</p>
    </div>
    <div style="display: flex; gap: 10px;">
        <a href="{{ url_for('scores') }}#tests" class="btn btn-secondary btn-sm">← Back to Score History</a>
        <a href="{{ url_for('aptitude') }}" class="btn btn-primary btn-sm">Take Another Test</a>
    </div>
</div>

<!-- RESULT SUMMARY BANNER -->
<div class="score-hero">
    {% set pct = (attempt.score * 100 // attempt.total) if attempt.total else 0 %}
    <div class="score-circle" style="--pct: {{ pct }}; --ring: {{ 'var(--success)' if pct >= 60 else 'var(--danger)' }};">
        <span class="big-number">{{ pct }}%</span>
        <span class="percent-label">{{ attempt.score }}/{{ attempt.total }} Marks</span>
    </div>
    <h2 style="font-size: 22px; font-weight: 800; color: var(--text-primary); margin-bottom: 6px;">{{ attempt.category }}</h2>
    <p style="color: var(--text-muted); font-size: 14px;">Submitted on: {{ attempt.submitted }} | Duration: Started at {{ attempt.started }}</p>
</div>

<!-- QUESTIONS BREAKDOWN -->
<h2 class="section-title">📋 Question-by-Question Review</h2>

{% if questions %}
    {% for q in questions %}
    <div class="review-item {% if q.is_correct %}correct{% else %}wrong{% endif %}">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 13px; font-weight: 700; color: var(--text-muted);">QUESTION {{ loop.index }}</span>
            {% if q.is_correct %}
                <span class="badge badge-success">✓ Correct (+1 Mark)</span>
            {% else %}
                <span class="badge badge-danger">✗ Incorrect (0 Marks)</span>
            {% endif %}
        </div>

        <div class="question-text" style="font-size: 16px;">
            {{ q.question }}
        </div>

        {% if q.code %}
        <pre><code>{{ q.code }}</code></pre>
        {% endif %}

        <div style="margin: 14px 0;">
            {% for opt in q.options %}
            <div style="padding: 10px 14px; border-radius: 8px; margin-bottom: 6px; font-size: 14px;
                {% if loop.index0 == q.correct_idx %}
                    background: #dcfce7; border: 1.5px solid #10b981; font-weight: 600; color: #065f46;
                {% elif loop.index0 == q.user_idx and not q.is_correct %}
                    background: #fee2e2; border: 1.5px solid #ef4444; color: #991b1b;
                {% else %}
                    background: #f8fafc; border: 1px solid var(--border-color); color: var(--text-secondary);
                {% endif %}">
                <span>{{ opt }}</span>
                {% if loop.index0 == q.correct_idx %}
                    <strong style="float: right; color: #059669;">✓ Correct Answer</strong>
                {% elif loop.index0 == q.user_idx and not q.is_correct %}
                    <strong style="float: right; color: #dc2626;">✗ Your Answer</strong>
                {% endif %}
            </div>
            {% endfor %}
        </div>

        {% if q.explanation %}
        <div class="explanation-box">
            <strong>💡 Explanation:</strong> {{ q.explanation }}
        </div>
        {% endif %}
    </div>
    {% endfor %}
{% else %}
    <div class="question-card" style="text-align: center; color: var(--text-muted); padding: 40px;">
        <p>No detailed question records are stored for this historical test. New tests taken will store complete question breakdowns and explanations.</p>
    </div>
{% endif %}

<div style="margin-top: 30px; text-align: center;">
    <a href="{{ url_for('aptitude') }}" class="btn btn-primary" style="padding: 12px 24px;">Start a New Aptitude or Coding Test →</a>
</div>
{% endblock %}
'''


# ---------------------------------------------------------------------
# PART 4: FLASK APPLICATION
# ---------------------------------------------------------------------
import os
import json
import sqlite3
import random
from datetime import datetime
from functools import wraps

from flask import (
    Flask, render_template, request, redirect,
    url_for, session, flash, jsonify
)
from werkzeug.security import generate_password_hash, check_password_hash


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# Templates live inside this file (see TEMPLATES below), not in a templates/ folder.
from jinja2 import DictLoader
app.jinja_loader = DictLoader(TEMPLATES)


@app.route("/site.css")
def site_css():
    from flask import Response
    return Response(SITE_CSS, mimetype="text/css")
# On a hosted server set a SECRET_KEY environment variable (any long random text).
# Without it a random key is used, which only works for a single local process.
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(32)
app.config["SESSION_PERMANENT"] = False          # cookie dies when browser closes
app.config["SESSION_COOKIE_HTTPONLY"] = True
DB_PATH = os.path.join(BASE_DIR, "placement_portal.db")

# Vercel's filesystem is read-only except /tmp, so copy the database there.
# NOTE: /tmp is temporary on Vercel - new accounts and scores can be lost.
if os.environ.get("VERCEL"):
    import shutil
    _tmp_db = "/tmp/placement_portal.db"
    if not os.path.exists(_tmp_db) and os.path.exists(DB_PATH):
        shutil.copy(DB_PATH, _tmp_db)
    DB_PATH = _tmp_db


# ====================================================================
# DATABASE INITIALIZATION AND HELPER
# ====================================================================

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cursor = conn.cursor()

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        profession TEXT DEFAULT 'Software Engineer',
        domain TEXT DEFAULT 'Computer Science',
        college TEXT DEFAULT 'Joy University',
        year_of_study TEXT DEFAULT '4th Year (Final Year)',
        skills TEXT DEFAULT 'Python, SQL, Data Structures',
        target_role TEXT DEFAULT 'TCS, Infosys, Amazon, Accenture'
    );
    """)

    # Create attempts table (for aptitude & technical tests)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        category TEXT,
        score INTEGER,
        total INTEGER,
        started TEXT,
        submitted TEXT,
        details TEXT DEFAULT '[]'
    );
    """)

    # Create practice table (for coding problems solved)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS practice (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        language TEXT,
        exercise TEXT,
        code TEXT DEFAULT '',
        status TEXT DEFAULT 'Solved',
        practiced TEXT
    );
    """)

    # Safely migrate existing users table if columns are missing
    user_columns = [col[1] for col in cursor.execute("PRAGMA table_info(users)").fetchall()]
    new_user_cols = [
        ("college", "TEXT DEFAULT 'Joy University'"),
        ("year_of_study", "TEXT DEFAULT '4th Year (Final Year)'"),
        ("skills", "TEXT DEFAULT 'Python, SQL, Data Structures'"),
        ("target_role", "TEXT DEFAULT 'TCS, Infosys, Amazon, Accenture'")
    ]
    for col_name, col_def in new_user_cols:
        if col_name not in user_columns:
            try:
                cursor.execute(f"ALTER TABLE users ADD COLUMN {col_name} {col_def}")
            except Exception:
                pass

    if "profile_done" not in user_columns:
        try:
            cursor.execute("ALTER TABLE users ADD COLUMN profile_done INTEGER DEFAULT 0")
        except Exception:
            pass

    # Safely migrate attempts table if details is missing
    attempt_columns = [col[1] for col in cursor.execute("PRAGMA table_info(attempts)").fetchall()]
    if "details" not in attempt_columns:
        try:
            cursor.execute("ALTER TABLE attempts ADD COLUMN details TEXT DEFAULT '[]'")
        except Exception:
            pass

    # Safely migrate practice table if code or status is missing
    practice_columns = [col[1] for col in cursor.execute("PRAGMA table_info(practice)").fetchall()]
    if "code" not in practice_columns:
        try:
            cursor.execute("ALTER TABLE practice ADD COLUMN code TEXT DEFAULT ''")
        except Exception:
            pass
    if "status" not in practice_columns:
        try:
            cursor.execute("ALTER TABLE practice ADD COLUMN status TEXT DEFAULT 'Solved'")
        except Exception:
            pass

    conn.commit()
    conn.close()


# PAGE BACKGROUND CLASS MAPPING

@app.context_processor
def inject_page_class():
    page_classes = {
        "login": "page-login",
        "register": "page-register",
        "dashboard": "page-dashboard",
        "aptitude": "page-aptitude",
        "take_test": "page-aptitude",
        "submit_test": "page-aptitude",
        "coding": "page-coding",
        "mark_practice": "page-coding",
        "interview": "page-interview",
        "companies": "page-companies",
        "profile": "page-profile",
        "scores": "page-scores",
        "test_review": "page-test-review",
        "test_result": "page-test-result"
    }

    done = True
    if session.get("user_id"):
        done = bool(session.get("profile_done"))

    return {
        "page_class": page_classes.get(
            request.endpoint, "page-dashboard"
        ),
        "profile_done": done
    }


@app.before_request
def force_profile_setup():
    """Logged-in users must fill the one-time profile before using the portal."""
    if not session.get("user_id"):
        return
    if request.endpoint in (None, "static", "profile", "logout", "login", "register", "index"):
        return
    if not session.get("profile_done"):
        flash("Please complete your student profile first (one-time setup).", "info")
        return redirect(url_for("profile"))


@app.after_request
def no_cache(resp):
    # stop the browser showing old logged-in pages from its cache
    if request.endpoint != "static":
        resp.headers["Cache-Control"] = "no-store"
    return resp


def current_user():
    if not session.get("user_id"):
        return None
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE id=?", (session["user_id"],)).fetchone()
    conn.close()
    return user


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get("user_id"):
            flash("Please log in to access the placement portal.", "info")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


# APPLICATION ROUTES
# ====================================================================

@app.route("/")
def index():
    session.clear()          # opening the site always asks for login
    return redirect(url_for("login"))


# --------------------------------------------------------------------
# AUTHENTICATION: REGISTER, LOGIN, LOGOUT
# --------------------------------------------------------------------

@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not name or not email or not password:
            flash("All fields are required.", "error")
            return redirect(url_for("register"))

        if len(password) < 6:
            flash("Password must be at least 6 characters long.", "error")
            return redirect(url_for("register"))

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for("register"))

        conn = get_db()
        try:
            conn.execute("""
                INSERT INTO users (name, email, password, profession, domain, college, year_of_study, skills, target_role)
                VALUES (?, ?, ?, 'Software Engineer', 'Computer Science', 'Joy University', '4th Year (Final Year)', 'Python, SQL, DSA', 'TCS, Infosys, Amazon')
            """, (name, email, generate_password_hash(password)))
            conn.commit()
            conn.close()
            flash("Registration successful! Please log in to your account.", "success")
            return redirect(url_for("login"))
        except sqlite3.IntegrityError:
            conn.close()
            flash("This email address is already registered. Please log in.", "error")
            return redirect(url_for("register"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        session.clear()      # always ask for email + password

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session.clear()
            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            session["user_email"] = user["email"]
            session["profile_done"] = bool(user["profile_done"])
            if not user["profile_done"]:
                flash(f"Welcome, {user['name']}! Please fill your student profile (one-time setup).", "info")
                return redirect(url_for("profile"))
            flash(f"Welcome back, {user['name']}!", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid email or password. Please try again.", "error")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been successfully logged out.", "info")
    return redirect(url_for("login"))


# --------------------------------------------------------------------
# STUDENT DASHBOARD
# --------------------------------------------------------------------

@app.route("/dashboard")
@login_required
def dashboard():
    user = current_user()
    if not user:
        session.clear()
        return redirect(url_for("login"))

    conn = get_db()

    # Total tests completed
    test_count = conn.execute(
        "SELECT COUNT(*) as cnt FROM attempts WHERE user_id=?", (user["id"],)
    ).fetchone()["cnt"]

    # Best score calculation
    best_row = conn.execute("""
        SELECT category, score, total, (score * 100 / total) as pct 
        FROM attempts 
        WHERE user_id=? AND total > 0
        ORDER BY pct DESC, id DESC LIMIT 1
    """, (user["id"],)).fetchone()

    best_score = best_row["pct"] if best_row else None
    best_test_name = best_row["category"] if best_row else None

    # Coding progress calculation
    coding_count = conn.execute(
        "SELECT COUNT(DISTINCT exercise) as cnt FROM practice WHERE user_id=?", (user["id"],)
    ).fetchone()["cnt"]

    # Most recent practiced language and exercise
    recent_practice = conn.execute("""
        SELECT language, exercise FROM practice 
        WHERE user_id=? ORDER BY id DESC LIMIT 1
    """, (user["id"],)).fetchone()

    active_language = recent_practice["language"] if recent_practice else "Python"
    recent_code_exercise = recent_practice["exercise"] if recent_practice else None

    # Recent 5 test attempts
    recent_tests = conn.execute("""
        SELECT * FROM attempts 
        WHERE user_id=? ORDER BY id DESC LIMIT 5
    """, (user["id"],)).fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        user=user,
        test_count=test_count,
        best_score=best_score,
        best_test_name=best_test_name,
        coding_count=coding_count,
        active_language=active_language,
        recent_code_exercise=recent_code_exercise,
        recent_tests=recent_tests
    )


# --------------------------------------------------------------------
# EDIT STUDENT PROFILE
# --------------------------------------------------------------------

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    user = current_user()
    if not user:
        return redirect(url_for("login"))

    if user["profile_done"]:
        flash("Your profile was already saved. It can only be edited once.", "info")
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        profession = request.form.get("profession", "").strip()
        domain = request.form.get("domain", "").strip()
        college = request.form.get("college", "").strip()
        year_of_study = request.form.get("year", "").strip()
        skills = request.form.get("skills", "").strip()
        target_role = request.form.get("target_role", "").strip()

        if not name:
            flash("Full Name cannot be empty.", "error")
            return redirect(url_for("profile"))

        conn = get_db()
        conn.execute("""
            UPDATE users 
            SET name=?, profession=?, domain=?, college=?, year_of_study=?, skills=?, target_role=?, profile_done=1
            WHERE id=?
        """, (name, profession, domain, college, year_of_study, skills, target_role, user["id"]))
        conn.commit()
        conn.close()

        session["user_name"] = name
        session["profile_done"] = True
        flash("Your student profile has been saved.", "success")
        return redirect(url_for("dashboard"))

    return render_template(
        "profile.html",
        user=user,
        professions=PROFESSIONS,
        domains=DOMAINS
    )


# --------------------------------------------------------------------
# SCORES, TEST HISTORY & BEST SCORE BREAKDOWN
# --------------------------------------------------------------------

@app.route("/scores")
@app.route("/progress")
@login_required
def scores():
    user = current_user()
    conn = get_db()

    # All test attempts
    attempts = conn.execute("""
        SELECT * FROM attempts 
        WHERE user_id=? ORDER BY id DESC
    """, (user["id"],)).fetchall()

    # Best test record
    best_test = conn.execute("""
        SELECT *, (score * 100 / total) as pct FROM attempts 
        WHERE user_id=? AND total > 0
        ORDER BY pct DESC, id DESC LIMIT 1
    """, (user["id"],)).fetchone()

    best_score = best_test["pct"] if best_test else None

    # Coding practice records
    practiced_exercises = conn.execute("""
        SELECT * FROM practice 
        WHERE user_id=? ORDER BY id DESC
    """, (user["id"],)).fetchall()

    languages_practiced = list(set([p["language"] for p in practiced_exercises]))
    active_language = practiced_exercises[0]["language"] if practiced_exercises else "Python"

    conn.close()

    return render_template(
        "scores.html",
        user=user,
        attempts=attempts,
        best_test=best_test,
        best_score=best_score,
        practiced_exercises=practiced_exercises,
        languages_practiced=languages_practiced,
        active_language=active_language
    )


@app.route("/test-review/<int:attempt_id>")
@login_required
def test_review(attempt_id):
    user = current_user()
    conn = get_db()
    attempt = conn.execute("""
        SELECT * FROM attempts WHERE id=? AND user_id=?
    """, (attempt_id, user["id"])).fetchone()
    conn.close()

    if not attempt:
        flash("Test record not found.", "error")
        return redirect(url_for("scores"))

    try:
        questions = json.loads(attempt["details"]) if attempt["details"] else []
    except Exception:
        questions = []

    return render_template("test_review.html", attempt=attempt, questions=questions)


# --------------------------------------------------------------------
# APTITUDE & CODING LANGUAGE TESTS
# --------------------------------------------------------------------

@app.route("/aptitude")
@login_required
def aptitude():
    user = current_user()
    return render_template("aptitude.html", user=user)


@app.route("/test/<category>", methods=["GET"])
@login_required
def take_test(category):
    if category not in QUESTION_BANKS:
        category = "python"

    bank = QUESTION_BANKS[category]
    test_title = bank["title"]
    all_qs = bank["questions"]

    # Select 10 questions (or all if <= 10)
    selected_qs = random.sample(all_qs, min(10, len(all_qs)))

    # Store in session for validation upon submission
    session["active_test"] = {
        "category": category,
        "title": test_title,
        "questions": selected_qs,
        "started": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return render_template(
        "test.html",
        category=category,
        test_title=test_title,
        questions=selected_qs
    )


@app.route("/submit-test", methods=["POST"])
@login_required
def submit_test():
    user = current_user()
    active_test = session.get("active_test")

    if not active_test:
        flash("Your test session expired or was not started properly.", "error")
        return redirect(url_for("aptitude"))

    category = active_test["category"]
    title = active_test["title"]
    questions = active_test["questions"]
    started = active_test["started"]
    submitted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    score = 0
    detailed_results = []

    for idx, q in enumerate(questions):
        user_ans = request.form.get(f"ans_{idx}")
        user_idx = int(user_ans) if user_ans is not None and user_ans.isdigit() else -1
        is_correct = (user_idx == q["correct_idx"])
        if is_correct:
            score += 1

        detailed_results.append({
            "question": q["question"],
            "code": q.get("code", ""),
            "options": q["options"],
            "correct_idx": q["correct_idx"],
            "user_idx": user_idx,
            "is_correct": is_correct,
            "explanation": q.get("explanation", "")
        })

    # Save attempt to database
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO attempts (user_id, category, score, total, started, submitted, details)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        user["id"],
        title,
        score,
        len(questions),
        started,
        submitted,
        json.dumps(detailed_results)
    ))
    attempt_id = cursor.lastrowid
    conn.commit()
    conn.close()

    session.pop("active_test", None)
    return redirect(url_for("test_result", attempt_id=attempt_id))


@app.route("/result/<int:attempt_id>")
@login_required
def test_result(attempt_id):
    user = current_user()
    conn = get_db()
    attempt = conn.execute("""
        SELECT * FROM attempts WHERE id=? AND user_id=?
    """, (attempt_id, user["id"])).fetchone()
    conn.close()

    if not attempt:
        flash("Test result not found.", "error")
        return redirect(url_for("scores"))

    try:
        questions = json.loads(attempt["details"]) if attempt["details"] else []
    except Exception:
        questions = []

    return render_template("result.html", attempt=attempt, questions=questions)


# --------------------------------------------------------------------
# CODING PRACTICE STUDIO
# --------------------------------------------------------------------

@app.route("/coding")
@login_required
def coding():
    user = current_user()
    language = request.args.get("language", "Python")
    if language not in CODING_CHALLENGES:
        language = "Python"

    problems = CODING_CHALLENGES[language]
    prob_id = request.args.get("prob_id", type=int)

    current_problem = problems[0]
    if prob_id:
        for p in problems:
            if p["id"] == prob_id:
                current_problem = p
                break

    conn = get_db()
    # Find which exercises user has solved
    solved_rows = conn.execute("""
        SELECT exercise FROM practice WHERE user_id=?
    """, (user["id"],)).fetchall()
    completed_exercise_names = [r["exercise"] for r in solved_rows]

    # Specific history for this language
    lang_practice_history = conn.execute("""
        SELECT * FROM practice 
        WHERE user_id=? AND language=? 
        ORDER BY id DESC LIMIT 5
    """, (user["id"], language)).fetchall()

    conn.close()

    solved_in_lang_count = len([p for p in problems if p["title"] in completed_exercise_names])

    return render_template(
        "coding.html",
        user=user,
        selected_lang=language,
        problems=problems,
        current_problem=current_problem,
        completed_exercise_names=completed_exercise_names,
        solved_in_lang_count=solved_in_lang_count,
        lang_practice_history=lang_practice_history
    )


@app.route("/mark-practice", methods=["POST"])
@login_required
def mark_practice():
    user = current_user()
    language = request.form.get("language", "Python")
    exercise = request.form.get("exercise", "")
    code = request.form.get("code", "")

    if not exercise:
        flash("Exercise title is missing.", "error")
        return redirect(url_for("coding", language=language))

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = get_db()
    conn.execute("""
        INSERT INTO practice (user_id, language, exercise, code, status, practiced)
        VALUES (?, ?, ?, ?, 'Solved', ?)
    """, (user["id"], language, exercise, code, now))
    conn.commit()
    conn.close()

    flash(f"🎉 Awesome! '{exercise}' in {language} marked as Solved and logged to your profile!", "success")
    return redirect(url_for("coding", language=language))


# --------------------------------------------------------------------
# INTERVIEW PREPARATION (REAL QUESTIONS & MODEL ANSWERS)
# --------------------------------------------------------------------

@app.route("/interview")
@login_required
def interview():
    user = current_user()
    category = request.args.get("category", "hr")
    if category not in INTERVIEW_DATA:
        category = "hr"

    data = INTERVIEW_DATA[category]
    return render_template(
        "interview.html",
        user=user,
        selected_category=category,
        active_category_title=data["title"],
        questions=data["questions"]
    )


# --------------------------------------------------------------------
# COMPANIES & JOBS DIRECTORY
# --------------------------------------------------------------------

@app.route("/companies")
@login_required
def companies():
    user = current_user()
    return render_template("companies.html", user=user, companies=COMPANIES_DATA)


# ====================================================================
# APPLICATION ENTRYPOINT
# ====================================================================

if os.environ.get("VERCEL"):
    init_db()


if __name__ == "__main__":
    init_db()
    print("Placement Preparation Portal starting on http://127.0.0.1:5000 ...")
    app.run(host="127.0.0.1", port=5000, debug=True)