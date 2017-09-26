"""Converts :term:`FASTA` to :term:`PHYLIP` format"""
import logging
import os

from Bio import SeqIO

from biokit.converters.base import ConvBase


def generate_outfile_name(infile, out_extension):
    """
    Replaces the file extension with the given one.
    :param infile: Input file
    :param out_extension: Desired extension
    :return: The filepath with the given extension
    """
    return '%s.%s' % (os.path.splitext(infile)[0], out_extension)


class fasta2phylip(ConvBase):
    """Converts a sequence alignment in :term:`FASTA` format to :term:`PHYLIP` format

    Conversion is based on Bio Python modules

    """

    input_ext = ['fa', 'fst', 'fasta', 'fn']
    output_ext = ['phylip', 'phy']

    def __init__(self, infile, outfile=None, alphabet=None, *args, **kwargs):
        """.. rubric:: constructor

        :param str infile: input fasta file.
        :param str outfile: input phylip file
        """
        if not outfile:
            outfile = generate_outfile_name(infile, 'phylip')
        super(fasta2phylip, self).__init__(infile, outfile)
        self.alphabet = alphabet

    def __call__(self):
        sequences = list(SeqIO.parse(self.infile, "fasta", alphabet=self.alphabet))
        count = SeqIO.write(sequences, self.outfile, "phylip")
        logging.debug("Converted %d records to phylip" % count)

