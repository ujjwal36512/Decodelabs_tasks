"""
Enterprise Random Password Generator
=====================================

A production-grade password generator implementing:
- Enterprise architecture with environmental requirements
- Character classification standardization
- Cryptographically secure randomness
- Memory-efficient string manipulation
- Linear time complexity optimization
- Mathematical security entropy calculation (E = L * log2(R))

Author: DecodeLabs Internship
"""

import os
import string
import math
import sys
from typing import Tuple, Dict, Optional
from dataclasses import dataclass
from enum import Enum
from secrets import SystemRandom, choice, shuffle


# ============================================================================
# ARCHITECTURE LAYER 1: Environment & Configuration
# ============================================================================

class PasswordComplexityLevel(Enum):
    """Define password complexity requirements for different security tiers."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    ENTERPRISE = "enterprise"


@dataclass
class EnvironmentalConfig:
    """
    Enterprise environmental configuration for password generation.
    Defines runtime constraints and security policies.
    """
    min_length: int
    max_length: int
    require_uppercase: bool
    require_lowercase: bool
    require_digits: bool
    require_special: bool
    exclude_ambiguous: bool
    complexity_level: PasswordComplexityLevel
    
    def validate(self) -> Tuple[bool, Optional[str]]:
        """Validate configuration constraints."""
        if self.min_length < 8:
            return False, "Minimum password length must be at least 8 characters"
        if self.min_length > self.max_length:
            return False, "Minimum length cannot exceed maximum length"
        if self.max_length > 256:
            return False, "Maximum password length cannot exceed 256 characters"
        return True, None


# ============================================================================
# ARCHITECTURE LAYER 2: Character Classification
# ============================================================================

class CharacterClassifier:
    """
    Standardized character classification using Python's string module.
    Provides memory-efficient character set management.
    """
    
    # Ambiguous characters that can be confused (0/O, 1/l/I, etc.)
    AMBIGUOUS_CHARS = set('0O1lI|`')
    
    # Special characters commonly used in passwords
    SPECIAL_CHARS_SAFE = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    SPECIAL_CHARS_EXTENDED = SPECIAL_CHARS_SAFE + '~`"\''
    
    def __init__(self, exclude_ambiguous: bool = False):
        """Initialize character classifier."""
        self.exclude_ambiguous = exclude_ambiguous
        self._cache: Dict[str, str] = {}
    
    def get_uppercase(self) -> str:
        """Get uppercase letters, excluding ambiguous chars if configured."""
        key = "uppercase"
        if key in self._cache:
            return self._cache[key]
        
        chars = string.ascii_uppercase
        if self.exclude_ambiguous:
            chars = ''.join(c for c in chars if c not in self.AMBIGUOUS_CHARS)
        
        self._cache[key] = chars
        return chars
    
    def get_lowercase(self) -> str:
        """Get lowercase letters, excluding ambiguous chars if configured."""
        key = "lowercase"
        if key in self._cache:
            return self._cache[key]
        
        chars = string.ascii_lowercase
        if self.exclude_ambiguous:
            chars = ''.join(c for c in chars if c not in self.AMBIGUOUS_CHARS)
        
        self._cache[key] = chars
        return chars
    
    def get_digits(self) -> str:
        """Get digits, excluding ambiguous chars if configured."""
        key = "digits"
        if key in self._cache:
            return self._cache[key]
        
        chars = string.digits
        if self.exclude_ambiguous:
            chars = ''.join(c for c in chars if c not in self.AMBIGUOUS_CHARS)
        
        self._cache[key] = chars
        return chars
    
    def get_special(self) -> str:
        """Get special characters."""
        key = "special"
        if key in self._cache:
            return self._cache[key]
        
        chars = self.SPECIAL_CHARS_EXTENDED
        if self.exclude_ambiguous:
            chars = ''.join(c for c in chars if c not in self.AMBIGUOUS_CHARS)
        
        self._cache[key] = chars
        return chars
    
    def get_all_characters(self, 
                          use_uppercase: bool = True,
                          use_lowercase: bool = True,
                          use_digits: bool = True,
                          use_special: bool = True) -> str:
        """Build complete character set based on requirements."""
        chars_list = []
        
        if use_uppercase:
            chars_list.append(self.get_uppercase())
        if use_lowercase:
            chars_list.append(self.get_lowercase())
        if use_digits:
            chars_list.append(self.get_digits())
        if use_special:
            chars_list.append(self.get_special())
        
        # Linear time complexity: O(n) where n is total characters
        return ''.join(chars_list)


# ============================================================================
# ARCHITECTURE LAYER 3: Cryptographic Security & Entropy
# ============================================================================

class SecurityAnalyzer:
    """
    Mathematical security analysis with entropy calculation.
    Formula: E = L * log2(R)
    Where: E = entropy (bits), L = password length, R = character pool size
    """
    
    def __init__(self):
        """Initialize security analyzer."""
        self.rng = SystemRandom()  # Cryptographically secure randomness
    
    @staticmethod
    def calculate_entropy(password_length: int, character_pool_size: int) -> float:
        """
        Calculate information entropy in bits.
        
        Formula: E = L * log2(R)
        - E: Entropy in bits
        - L: Password length
        - R: Character pool size (cardinality)
        
        Args:
            password_length: Length of the generated password
            character_pool_size: Number of unique characters available
            
        Returns:
            Entropy value in bits
        """
        if character_pool_size <= 1:
            return 0.0
        
        entropy = password_length * math.log2(character_pool_size)
        return entropy
    
    @staticmethod
    def security_rating(entropy: float) -> str:
        """
        Rate password security based on entropy value.
        
        Entropy Guidelines (NIST):
        - < 28 bits: Weak
        - 28-60 bits: Fair
        - 60-90 bits: Good
        - 90-128 bits: Strong
        - > 128 bits: Very Strong
        """
        if entropy < 28:
            return "Weak ⚠️"
        elif entropy < 60:
            return "Fair ⚡"
        elif entropy < 90:
            return "Good ✓"
        elif entropy < 128:
            return "Strong ✓✓"
        else:
            return "Very Strong ✓✓✓"
    
    def generate_random_bytes(self, length: int) -> bytes:
        """Generate cryptographically secure random bytes."""
        return os.urandom(length)
    
    def secure_random_choice(self, sequence: str) -> str:
        """Cryptographically secure random character selection."""
        return choice(sequence)


# ============================================================================
# ARCHITECTURE LAYER 4: Memory-Efficient String Manipulation
# ============================================================================

class PasswordBuilder:
    """
    Memory-efficient password builder using accumulator pattern.
    Optimized for linear time complexity O(n) where n is password length.
    """
    
    def __init__(self, rng: SystemRandom):
        """Initialize password builder with secure RNG."""
        self.rng = rng
        self._buffer: list = []  # Use list instead of string concatenation
    
    def add_random_char(self, charset: str) -> 'PasswordBuilder':
        """
        Add random character from charset. O(1) operation.
        
        Args:
            charset: String of characters to choose from
            
        Returns:
            Self for method chaining
        """
        if not charset:
            raise ValueError("Character set cannot be empty")
        
        char = choice(charset)
        self._buffer.append(char)
        return self
    
    def add_required_chars(self, requirements: Dict[str, str]) -> 'PasswordBuilder':
        """
        Add required characters for each category.
        O(k) where k is number of requirements.
        
        Args:
            requirements: Dict mapping requirement type to charset
            
        Returns:
            Self for method chaining
        """
        for charset in requirements.values():
            if charset:
                self.add_random_char(charset)
        return self
    
    def fill_random(self, target_length: int, charset: str) -> 'PasswordBuilder':
        """
        Fill buffer to target length with random characters.
        O(n - k) where n is target length and k is current buffer size.
        
        Args:
            target_length: Desired final password length
            charset: Character set for random selection
            
        Returns:
            Self for method chaining
        """
        while len(self._buffer) < target_length:
            self.add_random_char(charset)
        return self
    
    def shuffle(self) -> 'PasswordBuilder':
        """Shuffle password characters. O(n) operation."""
        shuffle(self._buffer)
        return self
    
    def build(self) -> str:
        """
        Build final password string. O(n) operation.
        Uses join() which is optimized in Python.
        
        Returns:
            Generated password
        """
        return ''.join(self._buffer)
    
    def clear(self) -> None:
        """Securely clear buffer. O(n) operation."""
        for i in range(len(self._buffer)):
            self._buffer[i] = '\x00'  # Overwrite with null bytes
        self._buffer.clear()
    
    def __len__(self) -> int:
        """Get current buffer length. O(1) operation."""
        return len(self._buffer)


# ============================================================================
# ARCHITECTURE LAYER 5: Enterprise Password Generator
# ============================================================================

class EnterprisePasswordGenerator:
    """
    Production-grade password generator combining all architectural layers.
    
    Features:
    - Cryptographically secure randomness
    - Configurable complexity requirements
    - Mathematical entropy analysis
    - Memory-efficient generation
    - Linear time complexity optimization
    """
    
    # Predefined configurations for different security levels
    PRESET_CONFIGS = {
        PasswordComplexityLevel.LOW: EnvironmentalConfig(
            min_length=8,
            max_length=12,
            require_uppercase=True,
            require_lowercase=True,
            require_digits=False,
            require_special=False,
            exclude_ambiguous=False,
            complexity_level=PasswordComplexityLevel.LOW
        ),
        PasswordComplexityLevel.MEDIUM: EnvironmentalConfig(
            min_length=12,
            max_length=16,
            require_uppercase=True,
            require_lowercase=True,
            require_digits=True,
            require_special=False,
            exclude_ambiguous=False,
            complexity_level=PasswordComplexityLevel.MEDIUM
        ),
        PasswordComplexityLevel.HIGH: EnvironmentalConfig(
            min_length=16,
            max_length=24,
            require_uppercase=True,
            require_lowercase=True,
            require_digits=True,
            require_special=True,
            exclude_ambiguous=True,
            complexity_level=PasswordComplexityLevel.HIGH
        ),
        PasswordComplexityLevel.ENTERPRISE: EnvironmentalConfig(
            min_length=24,
            max_length=32,
            require_uppercase=True,
            require_lowercase=True,
            require_digits=True,
            require_special=True,
            exclude_ambiguous=True,
            complexity_level=PasswordComplexityLevel.ENTERPRISE
        ),
    }
    
    def __init__(self, config: Optional[EnvironmentalConfig] = None):
        """
        Initialize enterprise password generator.
        
        Args:
            config: Environmental configuration. If None, uses MEDIUM preset.
        """
        self.config = config or self.PRESET_CONFIGS[PasswordComplexityLevel.MEDIUM]
        
        # Validate configuration
        is_valid, error_msg = self.config.validate()
        if not is_valid:
            raise ValueError(f"Invalid configuration: {error_msg}")
        
        self.classifier = CharacterClassifier(
            exclude_ambiguous=self.config.exclude_ambiguous
        )
        self.security = SecurityAnalyzer()
        self.rng = SystemRandom()
    
    def generate(self, length: Optional[int] = None) -> Tuple[str, Dict]:
        """
        Generate a secure password with security analysis.
        
        Time Complexity: O(n) where n is password length
        Space Complexity: O(n) for password storage
        
        Args:
            length: Custom password length. If None, uses random within min/max.
            
        Returns:
            Tuple of (password, security_analysis_dict)
        """
        # Determine password length
        if length is None:
            length = self.rng.randint(self.config.min_length, 
                                     self.config.max_length)
        
        if not (self.config.min_length <= length <= self.config.max_length):
            raise ValueError(
                f"Length {length} outside configured range "
                f"[{self.config.min_length}, {self.config.max_length}]"
            )
        
        # Build character set (O(n) where n is charset size)
        all_chars = self.classifier.get_all_characters(
            use_uppercase=self.config.require_uppercase,
            use_lowercase=self.config.require_lowercase,
            use_digits=self.config.require_digits,
            use_special=self.config.require_special
        )
        
        # Build requirements dict for mandatory characters
        requirements = {}
        if self.config.require_uppercase:
            requirements['uppercase'] = self.classifier.get_uppercase()
        if self.config.require_lowercase:
            requirements['lowercase'] = self.classifier.get_lowercase()
        if self.config.require_digits:
            requirements['digits'] = self.classifier.get_digits()
        if self.config.require_special:
            requirements['special'] = self.classifier.get_special()
        
        # Generate password using optimized builder (O(n) overall)
        builder = PasswordBuilder(self.rng)
        password = (builder
                   .add_required_chars(requirements)
                   .fill_random(length, all_chars)
                   .shuffle()
                   .build())
        
        # Calculate entropy and security metrics (O(1))
        entropy = self.security.calculate_entropy(len(password), len(all_chars))
        security_rating = self.security.security_rating(entropy)
        
        # Build analysis dictionary
        analysis = {
            'password': password,
            'length': len(password),
            'character_pool_size': len(all_chars),
            'entropy_bits': round(entropy, 2),
            'security_rating': security_rating,
            'complexity_level': self.config.complexity_level.value,
            'uppercase_included': self.config.require_uppercase,
            'lowercase_included': self.config.require_lowercase,
            'digits_included': self.config.require_digits,
            'special_included': self.config.require_special,
        }
        
        builder.clear()  # Securely clear builder buffer
        
        return password, analysis
    
    def generate_batch(self, count: int, 
                      length: Optional[int] = None) -> list:
        """
        Generate multiple passwords efficiently.
        
        Time Complexity: O(k * n) where k is count and n is length
        
        Args:
            count: Number of passwords to generate
            length: Custom password length for all passwords
            
        Returns:
            List of (password, analysis) tuples
        """
        return [self.generate(length) for _ in range(count)]


# ============================================================================
# ARCHITECTURE LAYER 6: Demonstration & Testing
# ============================================================================

def print_header(text: str, char: str = "=") -> None:
    """Print formatted header."""
    print(f"\n{char * 70}")
    print(f"{text.center(70)}")
    print(f"{char * 70}\n")


def demonstrate_generator():
    """Demonstrate enterprise password generator capabilities."""
    
    print_header("ENTERPRISE PASSWORD GENERATOR DEMONSTRATION")
    
    # =================================================================
    # 1. Low Complexity Passwords
    # =================================================================
    print_header("1. LOW COMPLEXITY PASSWORDS", "-")
    print("Configuration: 8-12 chars, Uppercase + Lowercase")
    
    gen_low = EnterprisePasswordGenerator(
        EnterprisePasswordGenerator.PRESET_CONFIGS[PasswordComplexityLevel.LOW]
    )
    
    for i in range(3):
        password, analysis = gen_low.generate()
        print(f"\nPassword {i+1}:")
        print(f"  Password: {password}")
        print(f"  Length: {analysis['length']}")
        print(f"  Entropy: {analysis['entropy_bits']} bits")
        print(f"  Security: {analysis['security_rating']}")
    
    # =================================================================
    # 2. Medium Complexity Passwords
    # =================================================================
    print_header("2. MEDIUM COMPLEXITY PASSWORDS", "-")
    print("Configuration: 12-16 chars, Uppercase + Lowercase + Digits")
    
    gen_medium = EnterprisePasswordGenerator(
        EnterprisePasswordGenerator.PRESET_CONFIGS[PasswordComplexityLevel.MEDIUM]
    )
    
    for i in range(3):
        password, analysis = gen_medium.generate()
        print(f"\nPassword {i+1}:")
        print(f"  Password: {password}")
        print(f"  Length: {analysis['length']}")
        print(f"  Entropy: {analysis['entropy_bits']} bits")
        print(f"  Security: {analysis['security_rating']}")
    
    # =================================================================
    # 3. High Complexity Passwords
    # =================================================================
    print_header("3. HIGH COMPLEXITY PASSWORDS", "-")
    print("Configuration: 16-24 chars, Uppercase + Lowercase + Digits + Special")
    print("(Excluding ambiguous characters)")
    
    gen_high = EnterprisePasswordGenerator(
        EnterprisePasswordGenerator.PRESET_CONFIGS[PasswordComplexityLevel.HIGH]
    )
    
    for i in range(3):
        password, analysis = gen_high.generate()
        print(f"\nPassword {i+1}:")
        print(f"  Password: {password}")
        print(f"  Length: {analysis['length']}")
        print(f"  Character Pool Size: {analysis['character_pool_size']}")
        print(f"  Entropy: {analysis['entropy_bits']} bits")
        print(f"  Security: {analysis['security_rating']}")
    
    # =================================================================
    # 4. Enterprise Complexity Passwords
    # =================================================================
    print_header("4. ENTERPRISE COMPLEXITY PASSWORDS", "-")
    print("Configuration: 24-32 chars, Full Requirements + No Ambiguous Chars")
    
    gen_enterprise = EnterprisePasswordGenerator(
        EnterprisePasswordGenerator.PRESET_CONFIGS[PasswordComplexityLevel.ENTERPRISE]
    )
    
    for i in range(3):
        password, analysis = gen_enterprise.generate()
        print(f"\nPassword {i+1}:")
        print(f"  Password: {password}")
        print(f"  Length: {analysis['length']}")
        print(f"  Character Pool Size: {analysis['character_pool_size']}")
        print(f"  Entropy: {analysis['entropy_bits']} bits")
        print(f"  Security: {analysis['security_rating']}")
    
    # =================================================================
    # 5. Entropy Analysis & Security Mathematics
    # =================================================================
    print_header("5. ENTROPY ANALYSIS & SECURITY MATHEMATICS", "-")
    print("Formula: E = L * log2(R)")
    print("Where: E = entropy (bits), L = password length, R = character pool size\n")
    
    security = SecurityAnalyzer()
    
    test_cases = [
        (8, 62, "8 chars from 62-char pool (letters + digits)"),
        (12, 94, "12 chars from 94-char pool (with special chars)"),
        (16, 85, "16 chars from 85-char pool (no ambiguous)"),
        (24, 85, "24 chars from 85-char pool (enterprise)"),
        (32, 85, "32 chars from 85-char pool (maximum)"),
    ]
    
    for length, pool_size, description in test_cases:
        entropy = security.calculate_entropy(length, pool_size)
        rating = security.security_rating(entropy)
        print(f"\n{description}")
        print(f"  Entropy = {length} * log2({pool_size}) = {entropy:.2f} bits")
        print(f"  Security Rating: {rating}")
    
    # =================================================================
    # 6. Time Complexity Analysis
    # =================================================================
    print_header("6. ALGORITHM COMPLEXITY ANALYSIS", "-")
    print("""
Time Complexity: O(n) - Linear
  - Password generation scales linearly with password length
  - Character set building: O(c) where c = charset size
  - Random character selection: O(1) average case
  - Shuffling: O(n) via Fisher-Yates
  - Overall: O(n) where n = password length

Space Complexity: O(n) - Linear
  - Password buffer storage: O(n)
  - Character set cache: O(c) - constant relative to password length
  - Overall: O(n) for password storage

Memory Efficiency:
  - Uses list accumulator pattern (not string concatenation)
  - String concatenation avoided (O(n²) in naive approach)
  - Secure buffer clearing after use
    """)
    
    # =================================================================
    # 7. Batch Generation Performance
    # =================================================================
    print_header("7. BATCH PASSWORD GENERATION", "-")
    print("Generating 5 enterprise passwords...\n")
    
    gen_batch = EnterprisePasswordGenerator(
        EnterprisePasswordGenerator.PRESET_CONFIGS[PasswordComplexityLevel.ENTERPRISE]
    )
    
    passwords = gen_batch.generate_batch(5)
    for idx, (pwd, analysis) in enumerate(passwords, 1):
        print(f"{idx}. {pwd} (Entropy: {analysis['entropy_bits']} bits)")
    
    # =================================================================
    # 8. Configuration Summary
    # =================================================================
    print_header("8. ARCHITECTURAL SUMMARY", "-")
    print("""
✓ Layer 1: Environmental Configuration
  - Predefined security levels (LOW, MEDIUM, HIGH, ENTERPRISE)
  - Configurable length constraints
  - Policy-based requirements

✓ Layer 2: Character Classification
  - Python string module standardization
  - Ambiguous character handling
  - Cached character set management

✓ Layer 3: Cryptographic Security
  - secrets.SystemRandom for secure randomness
  - os.urandom for cryptographic bytes
  - Mathematical entropy calculation
  - NIST-based security ratings

✓ Layer 4: Memory Optimization
  - Accumulator pattern with list buffer
  - Linear O(n) time complexity
  - Efficient string joining
  - Secure buffer clearing

✓ Layer 5: Enterprise Integration
  - Composable architecture
  - Extensible design
  - Production-ready error handling
  - Comprehensive analysis metadata

✓ Layer 6: Analysis & Metrics
  - Information entropy calculation
  - Security strength assessment
  - Performance characterization
  - Batch generation support
    """)


if __name__ == "__main__":
    try:
        demonstrate_generator()
        print("\n" + "=" * 70)
        print("DEMONSTRATION COMPLETED SUCCESSFULLY".center(70))
        print("=" * 70 + "\n")
    except Exception as e:
        print(f"\nError during demonstration: {e}", file=sys.stderr)
        sys.exit(1)
