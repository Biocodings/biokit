from biokit.converters.sam2bam import SAM2BAM
from biokit import biokit_data
from easydev import TempFile, md5

def test_conv():
    infile = biokit_data("converters/measles.sam")
    outfile = biokit_data("converters/measles.bam")
    with TempFile(suffix=".bam") as tempfile:
        convert = SAM2BAM(infile, tempfile.name)
        convert()

        # Check that the output is correct with a checksum
        # Note that we cannot test the md5 on a gzip file but only 
        # on the original data. This check sum was computed
        # fro the unzipped version of biokit/data/converters/measles.bed
        assert md5(tempfile.name) == md5(outfile)
        # 5cd453e698bccf942431618c945c226e
