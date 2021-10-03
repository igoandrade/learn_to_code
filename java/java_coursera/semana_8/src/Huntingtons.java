public class Huntingtons {

    // Returns the maximum number of consecutive repeats of CAG in the DNA string.
    public static int maxRepeats(String dna) {
        dna += "TTTTT";
        int maxRep = 0;
        int rep = 0;
        int i = 0;
        while (i < dna.length() - 3) {
            String t = dna.substring(i, i + 3);
            if (t.equals("CAG")) {
                rep = rep + 1;
                i = i + 3;
            } else {
                if (rep > maxRep) maxRep = rep;
                rep = 0;
                i = i + 1;
            }
        }
        return maxRep;
    }

    // Returns a copy of s, with all whitespace (spaces, tabs, and newlines) removed.
    public static String removeWhitespace(String s) {
        s = s.replace(" ", "");
        s = s.replace("\t", "");
        s = s.replace("\n", "");
        return s;
    }

    // Returns one of these diagnoses corresponding to the maximum number of repeats:
    // "not human", "normal", "high risk", or "Huntington's".
    public static String diagnose(int maxRepeats) {
        if (maxRepeats < 10) return "not human";
        if (maxRepeats < 36) return "normal";
        if (maxRepeats < 40) return "high risk";
        if (maxRepeats < 181) return "Huntington's";
        return "not human";
    }

    // Sample client (see below).
    public static void main(String[] args) {
        In in = new In(args[0]);
        String dna = in.readAll();
        dna = removeWhitespace(dna);
        int maxRep = maxRepeats(dna);
        String diag = diagnose(maxRep);
        StdOut.println("max repeats = " + maxRep + "\n" + diag);
    }

}