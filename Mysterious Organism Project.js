// Returns a random DNA base
const returnRandBase = () => {
  const dnaBases = ['A', 'T', 'C', 'G']
  return dnaBases[Math.floor(Math.random() * 4)] 
}

// Returns a random single strand of DNA containing 15 bases
const mockUpStrand = () => {
  const newStrand = []
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase())
  }
  return newStrand
}

// Function that takes a number and an array of DNA bases as parameters and returns an object
const pAequorFactory = (num, arr) => {
  return {
    specimenNum: num,
    dna: arr,

    // Randomly selects a base in the dna array ad changes it to a different base, ensuring the new base is not the same as the original
    mutate() {
      const randomIndex = Math.floor(Math.random() * this.dna.length);
      let newBase = returnRandBase();
      while (this.dna[randomIndex] === newBase) {
        newBase = returnRandBase();
      }
      this.dna[randomIndex] = newBase;
      return this.dna;
    },

    // Compares the DNA of the current specimen with another specimen, calculates the percentage of identical bases, and prints a message
    compareDNA(otherPAequor) {
      let identicalBases = 0;
      for (let i = 0; i < this.dna.length; i++) {
        if (this.dna[i] === otherPAequor.dna[i]) {
          identicalBases++;
        };
      };
      const percentage = (identicalBases / this.dna.length) * 100;
      console.log(`specimen #${this.specimenNum} and specimen #${otherPAequor.specimenNum} have ${percentage.toFixed(2)}% DNA in common.`)
    },

    // Checks the likely chance of survival if dna is made up of at least 60% 'C' or 'G' bases (Return true >= 60|Return flase < 60)
    willLikelySurvive() {
      let count = 0;
      for (let i = 0; i < this.dna.length; i++) {
        if (this.dna[i] === 'C' || this.dna[i] === 'G') {
          count++;
        }
      }
      const percentage = (count / this.dna.length) * 100;
      return percentage >= 60;
    },

    // Function that takes a number and an array of DNA bases as parameters and returns an object
    complementStrand() {
      return this.dna.map(base => {
        switch(base) {
          case 'A':
            return 'T';
          case 'T':
            return 'A';
          case 'C':
            return 'G';
          case 'G':
            return 'C';
        }
      });
    }

  };
};

// Example usage:
/* const specimen = pAequorFactory(1, mockUpStrand());
console.log(specimen.dna);
console.log(specimen.mutate()); */

// Example usage of .compareDNA():
/* const specimen1 = pAequorFactory(1, mockUpStrand());
const specimen2 = pAequorFactory(2, mockUpStrand());
specimen1.compareDNA(specimen2); */

// Example usage of .willLikelySurvive():
/* const specimen = pAequorFactory(1, mockUpStrand());
console.log(specimen.willLikelySurvive()); */


// 30 Instances of pAequor that can survive their natural environment
const survivingSpecimens = [];
let id = 1;

while (survivingSpecimens.length < 30) {
  const newSpecimen = pAequorFactory(id, mockUpStrand());
  if (newSpecimen.willLikelySurvive()) {
    survivingSpecimens.push(newSpecimen);
  }
  id++;
}

console.log(survivingSpecimens);

