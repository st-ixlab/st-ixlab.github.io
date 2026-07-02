require 'bibtex'

module BibTeX
  class Entry
    alias_method :original_get_field_for_scholar, :[]

    MONTH_MAP = {
      'jan' => 1, 'january' => 1,
      'feb' => 2, 'february' => 2,
      'mar' => 3, 'march' => 3,
      'apr' => 4, 'april' => 4,
      'may' => 5,
      'jun' => 6, 'june' => 6,
      'jul' => 7, 'july' => 7,
      'aug' => 8, 'august' => 8,
      'sep' => 9, 'september' => 9,
      'oct' => 10, 'october' => 10,
      'nov' => 11, 'november' => 11,
      'dec' => 12, 'december' => 12
    }.freeze

    def [](key)
      val = original_get_field_for_scholar(key)
      k = key.to_s.downcase

      if k == 'type' && (val.nil? || val.to_s.empty?)
        self.type.to_s
      elsif k == 'month_numeric' || k == 'month_desc' || k == 'month'
        raw_month = original_get_field_for_scholar(:month) || original_get_field_for_scholar('month')
        if raw_month
          m_str = raw_month.to_s.strip.downcase.gsub(/[^a-z0-9]/, '')
          m_num = MONTH_MAP[m_str] || m_str.to_i
          m_num = 0 if m_num <= 0 || m_num > 12

          if k == 'month_desc'
            sprintf('%02d', 99 - m_num)
          else
            sprintf('%02d', m_num)
          end
        else
          k == 'month_desc' ? '99' : '00'
        end
      else
        val
      end
    end
  end
end
