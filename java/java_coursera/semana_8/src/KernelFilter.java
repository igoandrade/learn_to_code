import java.awt.Color;

public class KernelFilter {
    // Returns a new picture that applies the identity filter to the given picture.
    public static Picture identity(Picture picture) {
        int[][] kernel = { 
            {0, 0, 0}, 
            {0, 1, 0}, 
            {0, 0, 0} 
        };
        int length = kernel.length;
        int w = picture.width();
        int h = picture.height();
        Picture pic = new Picture(w, h);
        for (int col = 0; col < w; col++) {
            for (int row = 0; row < h; row++) {
                int newR = 0;
                int newG = 0;
                int newB = 0;
                int n = length / 2;
                for (int i = 0; i < length; i++) {
                    int c = (col - n + i + w) % w;
                    for (int j = 0; j < length; j++) {
                        int r = (row - n + j + h) % h;
                        Color oldColor = picture.get(c, r);
                        int oldR = oldColor.getRed();
                        int oldG = oldColor.getGreen();
                        int oldB = oldColor.getBlue();
                        newR += kernel[j][i] * oldR;
                        newG += kernel[j][i] * oldG;
                        newB += kernel[j][i] * oldB;
                    }
                }
                if (newR < 0) newR = 0;
                if (newR > 255) newR = 255;
                if (newG < 0) newG = 0;
                if (newG > 255) newG = 255;
                if (newB < 0) newB = 0;
                if (newB > 255) newB = 255;
                Color newColor = new Color(newR, newG, newB);
                pic.set(col, row, newColor);
            }
        }
        return pic;
    }

    // Returns a new picture that applies a Gaussian blur filter to the given picture.
    public static Picture gaussian(Picture picture) {
        double[][] kernel = { 
            {1.0/16.0, 2.0/16.0, 1.0/16.0}, 
            {2.0/16.0, 4.0/16.0, 2.0/16.0}, 
            {1.0/16.0, 2.0/16.0, 1.0/16.0} 
        };
        int length = kernel.length;
        int w = picture.width();
        int h = picture.height();
        Picture pic = new Picture(w, h);
        for (int col = 0; col < w; col++) {
            for (int row = 0; row < h; row++) {
                int newR = 0;
                int newG = 0;
                int newB = 0;
                int n = length / 2;
                for (int i = 0; i < length; i++) {
                    int c = (col - n + i + w) % w;
                    for (int j = 0; j < length; j++) {
                        int r = (row - n + j + h) % h;
                        Color oldColor = picture.get(c, r);
                        int oldR = oldColor.getRed();
                        int oldG = oldColor.getGreen();
                        int oldB = oldColor.getBlue();
                        newR += kernel[j][i] * oldR;
                        newG += kernel[j][i] * oldG;
                        newB += kernel[j][i] * oldB;
                    }
                }
                newR = (int) Math.ceil(newR);
                if (newR < 0) newR = 0;
                if (newR > 255) newR = 255;
                newG = (int) Math.ceil(newG);
                if (newG < 0) newG = 0;
                if (newG > 255) newG = 255;
                newB = (int) Math.ceil(newB);
                if (newB < 0) newB = 0;
                if (newB > 255) newB = 255;
                Color newColor = new Color(newR, newG, newB);
                pic.set(col, row, newColor);
            }
        }
        return pic;
    }

    // Returns a new picture that applies a sharpen filter to the given picture.
    public static Picture sharpen(Picture picture) {
        int[][] kernel = { 
            { 0, -1,  0}, 
            {-1,  5, -1}, 
            { 0, -1,  0} 
        };
        int length = kernel.length;
        int w = picture.width();
        int h = picture.height();
        Picture pic = new Picture(w, h);
        for (int col = 0; col < w; col++) {
            for (int row = 0; row < h; row++) {
                int newR = 0;
                int newG = 0;
                int newB = 0;
                int n = length / 2;
                for (int i = 0; i < length; i++) {
                    int c = (col - n + i + w) % w;
                    for (int j = 0; j < length; j++) {
                        int r = (row - n + j + h) % h;
                        Color oldColor = picture.get(c, r);
                        int oldR = oldColor.getRed();
                        int oldG = oldColor.getGreen();
                        int oldB = oldColor.getBlue();
                        newR += kernel[j][i] * oldR;
                        newG += kernel[j][i] * oldG;
                        newB += kernel[j][i] * oldB;
                    }
                }
                if (newR < 0) newR = 0;
                if (newR > 255) newR = 255;
                if (newG < 0) newG = 0;
                if (newG > 255) newG = 255;
                if (newB < 0) newB = 0;
                if (newB > 255) newB = 255;
                Color newColor = new Color(newR, newG, newB);
                pic.set(col, row, newColor);
            }
        }
        return pic;
    }

    // Returns a new picture that applies an Laplacian filter to the given picture.
    public static Picture laplacian(Picture picture) {
        int[][] kernel = { 
            {-1, -1, -1}, 
            {-1,  8, -1}, 
            {-1, -1, -1} 
        };
        int length = kernel.length;
        int w = picture.width();
        int h = picture.height();
        Picture pic = new Picture(w, h);
        for (int col = 0; col < w; col++) {
            for (int row = 0; row < h; row++) {
                int newR = 0;
                int newG = 0;
                int newB = 0;
                int n = length / 2;
                for (int i = 0; i < length; i++) {
                    int c = (col - n + i + w) % w;
                    for (int j = 0; j < length; j++) {
                        int r = (row - n + j + h) % h;
                        Color oldColor = picture.get(c, r);
                        int oldR = oldColor.getRed();
                        int oldG = oldColor.getGreen();
                        int oldB = oldColor.getBlue();
                        newR += kernel[j][i] * oldR;
                        newG += kernel[j][i] * oldG;
                        newB += kernel[j][i] * oldB;
                    }
                }
                if (newR < 0) newR = 0;
                if (newR > 255) newR = 255;
                if (newG < 0) newG = 0;
                if (newG > 255) newG = 255;
                if (newB < 0) newB = 0;
                if (newB > 255) newB = 255;
                Color newColor = new Color(newR, newG, newB);
                pic.set(col, row, newColor);
            }
        }
        return pic;
    }

    // Returns a new picture that applies an emboss filter to the given picture.
    public static Picture emboss(Picture picture) {
        int[][] kernel = { 
            {-2, -1, 0}, 
            {-1,  1, 1}, 
             {0,  1, 2} 
        };
        int length = kernel.length;
        int w = picture.width();
        int h = picture.height();
        Picture pic = new Picture(w, h);
        int n = length / 2;
        for (int col = 0; col < w; col++) {
            for (int row = 0; row < h; row++) {
                int newR = 0;
                int newG = 0;
                int newB = 0;
                for (int i = 0; i < length; i++) {
                    int c = (col - n + i + w) % w;
                    for (int j = 0; j < length; j++) {
                        int r = (row - n + j + h) % h;
                        Color oldColor = picture.get(c, r);
                        int oldR = oldColor.getRed();
                        int oldG = oldColor.getGreen();
                        int oldB = oldColor.getBlue();
                        newR += kernel[j][i] * oldR;
                        newG += kernel[j][i] * oldG;
                        newB += kernel[j][i] * oldB;
                    }
                }
                if (newR < 0) newR = 0;
                if (newR > 255) newR = 255;
                if (newG < 0) newG = 0;
                if (newG > 255) newG = 255;
                if (newB < 0) newB = 0;
                if (newB > 255) newB = 255;
                Color newColor = new Color(newR, newG, newB);
                pic.set(col, row, newColor);
            }
        }
        return pic;
    }

    // Returns a new picture that applies a motion blur filter to the given picture.
    public static Picture motionBlur(Picture picture) {
        double[][] kernel = new double[9][9];
        for (int i = 0; i < 9; i++) {
            kernel[i][i] = 1.0/9.0;
        }
        int length = kernel.length;
        int w = picture.width();
        int h = picture.height();
        Picture pic = new Picture(w, h);
        for (int col = 0; col < w; col++) {
            for (int row = 0; row < h; row++) {
                int newR = 0;
                int newG = 0;
                int newB = 0;
                int n = length / 2;
                for (int i = 0; i < length; i++) {
                    int c = (col - n + i + w) % w;
                    for (int j = 0; j < length; j++) {
                        int r = (row - n + j + h) % h;
                        Color oldColor = picture.get(c, r);
                        int oldR = oldColor.getRed();
                        int oldG = oldColor.getGreen();
                        int oldB = oldColor.getBlue();
                        newR += kernel[j][i] * oldR;
                        newG += kernel[j][i] * oldG;
                        newB += kernel[j][i] * oldB;
                    }
                }
                newR = (int) Math.ceil(newR);
                if (newR < 0) newR = 0;
                if (newR > 255) newR = 255;
                newG = (int) Math.ceil(newG);
                if (newG < 0) newG = 0;
                if (newG > 255) newG = 255;
                newB = (int) Math.ceil(newB);
                if (newB < 0) newB = 0;
                if (newB > 255) newB = 255;
                Color newColor = new Color(newR, newG, newB);
                pic.set(col, row, newColor);
            }
        }
        return pic;
    }

    // Test client (ungraded).
    public static void main(String[] args) {
        Picture pic = new Picture(args[0]);
        pic = identity(pic);
        pic = emboss(pic);
        pic = laplacian(pic);
        pic = gaussian(pic);
        pic = sharpen(pic);
        pic = motionBlur(pic);
        pic.show();
    }

}